from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import numpy as np
from typing import List

model_id = "openai/clip-vit-base-patch32"

# Load model and processor
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)

def get_image_embedding_from_path(image_path: str) -> List[float]:
    """
    Opens an image from a file path and returns its embedding.
    """
    image = Image.open(image_path).convert("RGB")
    return get_image_embedding_from_image(image)

def get_image_embedding_from_image(image: Image.Image) -> List[float]:
    """
    Takes a PIL Image, processes it through the CLIP model,
    and returns its embedding as a list of floats.
    """
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.get_image_features(**inputs)
    return outputs.detach().numpy()[0].tolist()

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Computes the cosine similarity between two vectors.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    epsilon = 1e-8  
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2) + epsilon))
