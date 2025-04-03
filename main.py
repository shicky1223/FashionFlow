from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from model import (
    cosine_similarity,
    get_image_embedding_from_path,
    get_image_embedding_from_image
)
from PIL import Image
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class WardrobeItem(BaseModel):
    id: int
    name: str
    description: str
    image_url: str
    embedding: List[float]  


wardrobe_db = []

@app.post("/upload-item", response_model=WardrobeItem)
async def upload_item(item: WardrobeItem, image: UploadFile = File(...)):
    wardrobe_db.append(item)
    return item

@app.get("/wardrobe", response_model=List[WardrobeItem])
async def get_wardrobe():
    return wardrobe_db

@app.post("/similar-items")
async def similar_items(
    image: Optional[UploadFile] = File(None),
    image_path: Optional[str] = Query(None, description="Local path to the image file")
):
    # Ensure that at least one method of image input is provided.
    if image is None and image_path is None:
        raise HTTPException(status_code=400, detail="Provide an image file or an image_path.")

    # Compute image embedding from either an uploaded image or a local file path.
    if image:
        contents = await image.read()
        image_obj = Image.open(io.BytesIO(contents)).convert("RGB")
        image_embedding = get_image_embedding_from_image(image_obj)
    else:
        image_embedding = get_image_embedding_from_path(image_path)
    
    similarities = []
    for item in wardrobe_db:
        if not item.embedding:
            continue
        similarity = cosine_similarity(image_embedding, item.embedding)
        similarities.append((similarity, item))
    
    similarities.sort(key=lambda x: x[0], reverse=True)
    
    similar_items_list = [item.dict() for sim, item in similarities]
    return {"similar_items": similar_items_list}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
