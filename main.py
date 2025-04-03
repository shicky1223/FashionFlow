# main.py
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
import uvicorn
from model import cosine_similarity, get_image_embedding  # Corrected import statement
from PIL import Image
import io

app = FastAPI()

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
async def similar_items(image: UploadFile = File(...)):
    contents = await image.read()
    image_obj = Image.open(io.BytesIO(contents)).convert("RGB")
    
    image_embedding = get_image_embedding(image_obj)
    
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
