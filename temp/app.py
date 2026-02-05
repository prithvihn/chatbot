import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Initialize conversation history
messages = [
    SystemMessage("You are a helpful assistant."),
]

print("Assistant: Hello! How can I assist you today?")
print("(Type 'exit' to quit)\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if not user_input:
        continue
    
    # Add user message to history
    messages.append(UserMessage(user_input))
    
    try:
        response = client.complete(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model
        )
        
        assistant_message = response.choices[0].message.content
        print(f"\nAssistant: {assistant_message}\n")
        
        # Add assistant response to history
        messages.append(SystemMessage(assistant_message))
        
    except Exception as e:
        print(f"\nError: {str(e)}\n")

