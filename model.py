from transformers import pipeline 
messages = [
    {"roles":"user", "content": "Who are you?"}
    ]
model_id = "SentientAGI/Dobby-Mini-Unhinged-Llama-3.1-8B"
pipe = pipeline("text-generation", model = model_id )

pipe(messages)
