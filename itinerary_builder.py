from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def build_itinerary(prompt):
    response = generator(prompt, max_length=200, num_return_sequences=1)
    return response[0]["generated_text"]

# Example
user_prompt = "Plan a 5-day trip to Paris for a couple interested in art and food"
print(build_itinerary(user_prompt))
