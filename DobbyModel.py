from transformers import pipeline


def load_dobby_model(model_name = "Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B"):
   generator = pipeline(
    "text-generation",
    model="Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B",
    tokenizer="Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B",
    trust_remote_code=True,)
   return generator


if __name__ == "__main__":
    # Load the Dobby model using our function
    generator = load_dobby_model()

    # Define a prompt for text generation
    prompt = "Generate an engaging description for an outfit that blends modern streetwear with vintage flair."

<<<<<<< HEAD
    # Generate text using the loaded model
=======
# Function to generate an outfit description using Dobby
def generate_outfit_description(prompt: str):
>>>>>>> 6817560d768add9eae5c39f5efeaac926cd3d4d9
    outputs = generator(
        prompt,
        max_length=256,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.65,
        top_p=0.9
    )
<<<<<<< HEAD
=======
    return outputs[0]['generated_text']

# Function to get the image embedding from CLIP
def get_image_embedding(image_path: str):
    image = Image.open(image_path)
    # Process the image for CLIP
    inputs = clip_processor(images=image, return_tensors="pt", padding=True)
    # Get image features
    outputs = clip_model.get_image_features(**inputs)
    embedding = outputs.detach().numpy()
    return embedding

# Function to calculate the similarity between the image and a prompt (text)
def get_image_text_similarity(image_path: str, text_prompt: str):
    image = Image.open(image_path)
    # Process the image and text
    inputs = clip_processor(text=[text_prompt], images=image, return_tensors="pt", padding=True)
    # Get similarity scores
    outputs = clip_model(**inputs)
    similarity_score = torch.cosine_similarity(outputs.image_embeds, outputs.text_embeds)
    return similarity_score.item()

prompt = "Generate an engaging description for an outfit that blends modern streetwear with vintage flair."
outputs = generator(
    prompt,
    max_length=256,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.65,
    top_p=0.9
)
>>>>>>> 6817560d768add9eae5c39f5efeaac926cd3d4d9

    # Print the generated text
    print(outputs[0]['generated_text'])