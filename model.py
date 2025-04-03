from transformers import CLIPProcessor, CLIPModel
from PIL import Image

model_id = "openai/clip-vit-base-patch32"

# Load model and processor
model = CLIPModel.from_pretrained(model_id)
processor = CLIPProcessor.from_pretrained(model_id)
