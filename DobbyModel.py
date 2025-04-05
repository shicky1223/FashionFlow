from transformers import pipeline

# Create a text generation pipeline using Dobby
generator = pipeline(
    "text-generation",
    model="Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B",
    tokenizer="Sentientagi/Dobby-Mini-Unhinged-Llama-3.1-8B",
    trust_remote_code=True,
)

prompt = "Generate an engaging description for an outfit that blends modern streetwear with vintage flair."
outputs = generator(
    prompt,
    max_length=256,
    num_return_sequences=1,
    do_sample=True,
    temperature=0.65,
    top_p=0.9
)

print(outputs[0]['generated_text'])
