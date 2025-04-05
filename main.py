import io 
from fastapi import FastAPI, File, UploadFile
from CLIPModelintegration import load_clip_model
from PIL import Image

app = FastAPI()
model, processor = load_clip_model()

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    inputs = processor(images=image, return_tensors="pt", padding=True)
    outputs = model.get_image_features(**inputs)
    embedding = outputs.detach().numpy().tolist()  # Convert to list for JSON serialization
    return {"embedding": embedding}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)