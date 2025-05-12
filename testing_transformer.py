from transformers import pipeline


pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-hf", truncation=True)
output = pipe("What is the capital of Brazil?", max_length=50, num_return_sequences=1)
print(output[0]['generated_text'])
# The above code uses the Hugging Face Transformers library to create a text generation pipeline using the GPT-2 model.