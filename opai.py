from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Generate text
text = generator("Once upon a time", max_length=100, do_sample=True)[0]

print(text['generated_text'])


