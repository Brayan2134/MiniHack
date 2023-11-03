import openai

# Set your API key
api_key = "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"
openai.api_key = api_key

# Initialize the conversation with a system message
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
]

# Main conversation loop
while True:
    user_input = input("\n" + "User: ")
    
    # Add the user's message to the conversation
    conversation.append({"role": "user", "content": user_input})
    
    # Keep the conversation within token limits (e.g., truncate or remove old messages)
    while len(conversation) > 10:
        conversation.pop(0)
    
    # Generate a response from the assistant
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    
    assistant_response = response['choices'][0]['message']['content']
    print("\n" + "Assistant:", assistant_response)
