import openai
openai.api_key = "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" # replace with your own API key

# set up the model and parameters
model_engine = "text-davinci-002" # or any other GPT-4 model engine
prompt = "Hello, how can I assist you?" # or any other initial prompt

# define a function to generate a response from the model
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# get input from the user and generate a response
while True:
    user_input = input("You: ")
    prompt += user_input.strip() + "\n"
    response = generate_response(prompt)
    print("ChatGPT-4: " + response)
