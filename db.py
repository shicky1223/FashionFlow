from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import io 
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import numpy as np
import faiss
from CLIPModelintegration import load_clip_model

CLIPmodel, processor  = load_clip_model()
embedding_dim = 512
index = faiss.IndexFlatL2(embedding_dim)

#Setup faiss db
metadata_store = [] #change to a database 

app = FastAPI()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    inputs = processor(images=image, return_tensors="pt", padding=True)
    outputs = CLIPmodel.get_image_features(**inputs)
    embedding = outputs.detach().numpy().tolist()  # Convert to list for JSON serialization
    if embedding.shape[1] != embedding_dim:
        raise HTTPException(status_code=500, detail="Embedding dimension mismatch.")
    index.add(embedding) #add the embedding to the FAISS index
    metadata_store.append(file.filename)
    return {"embedding": embedding.tolist(), "message": "Image embedding stored successfully."}


@app.get("/search")
def search(query_index: int, k: int = 5):
    if query_index < 0  or query_index >= len(metadata_store):
        raise HTTPException(status_code=404, detail="Query index out of bounds.")

    # Reconstruct the vector of the query image from the index
    query_vector = index.reconstruct(query_index)
    query_vector = np.expand_dims(query_vector, axis=0) 

    #perform distance search on the index

    distances, indicies = index.search(query_vector, k)
    results = []
    for dist, idx in zip(distances[0], indicies[0]):
        result = {
            "index": int(idx),
            "distance": float(dist),
            "filename": metadata_store[idx] if idx < len(metadata_store) else "N/A"
        }
        results.append(result)
    
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)