from transformers import CLIPProcessor, CLIPModel
from PIL import Image
def load_clip_model(model_name = "openai/clip-vit-base-patch32"):
    model = CLIPModel.from_pretrained(model_name)
    processor = CLIPProcessor.from_pretrained(model_name)
    return model, processor

def get_image_embedding(image_path, model, processor):
    image = Image.open(image_path)
    #Process the image without text prompts 
    inputs = processor(images = image, return_tensors ="pt", padding = True)
    outputs = model.get_image_features(**inputs)
    embedding = outputs.detach().numpy()
    return embedding

if __name__ == "__main__":
    model, processor = load_clip_model()
    embedding = get_image_embedding("/Users/shicky/FashionFlow/1024x1024-Womens-Jackets-Racer-Black-102722-1.jpg" ,model, processor)
    print("Image embedding shape:", embedding.shape)

