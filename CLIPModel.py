from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# Load model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Open an image and create input
image = Image.open("path/to/your/image.jpg")
inputs = processor(text=["a stylish jacket"], images=image, return_tensors="pt", padding=True)

# Get embeddings and similarity scores
outputs = clip_model(**inputs)
image_embeds = outputs.image_embeds
text_embeds = outputs.text_embeds
# You can now compare embeddings using cosine similarity
