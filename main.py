import io 
from fastapi import FastAPI, File, UploadFile
from CLIPModelintegration import load_clip_model
from transformers import pipeline
from PIL import Image
from DobbyModel import generator

app = FastAPI()
CLIPmodel, processor = load_clip_model()

generator = pipeline(
    "text-generation",
    model="Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B",
    tokenizer="Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B",
    trust_remote_code=True,
)

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    inputs = processor(images=image, return_tensors="pt", padding=True)
    outputs = CLIPmodel.get_image_features(**inputs)
    embedding = outputs.detach().numpy().tolist()  # Convert to list for JSON serialization
    return {"embedding": embedding}

@app.post("/generate-description")
async def generate_description(prompt: str):
    outputs = generator(
        prompt,
        max_length=256,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.65,
        top_p=0.9
    )
    return {"generated_description": outputs[0]['generated_text']}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
