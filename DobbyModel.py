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

    # Generate text using the loaded model
    outputs = generator(
        prompt,
        max_length=256,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.65,
        top_p=0.9
    )

    # Print the generated text
    print(outputs[0]['generated_text'])