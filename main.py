# main.py
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

class WardrobeItem(BaseModel):
    id: int
    name: str
    description: str
    image_url: str

wardrobe_db = []  # This will act as a dummy in-memory store

@app.post("/upload-item", response_model=WardrobeItem)
async def upload_item(item: WardrobeItem, image: UploadFile = File(...)):
    # Here you would process and save the image, then store the item details in your database.
    wardrobe_db.append(item)
    return item

@app.get("/wardrobe", response_model=List[WardrobeItem])
async def get_wardrobe():
    return wardrobe_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
