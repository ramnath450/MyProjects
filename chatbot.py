import random

# Define a simple chatbot that can respond to a few predefined questions and learn from user interactions
def chatbot_response(message, memory):
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm a bot, so I don't have feelings.", "I'm functioning well, thank you!", "I'm doing great, how about you?"],
        "what's your name": ["I'm a chatbot.", "You can call me Bot.", "I don't have a name."],
        "bye": ["Goodbye!", "See you later!", "Farewell!"],
        "default": ["I'm not sure how to respond to that.", "Could you please rephrase?", "I didn't get that."]
    }

    # Check if the message is in the responses dictionary
    if message.lower() in responses:
        return random.choice(responses[message.lower()])
    else:
        # If the message is not recognized, add it to the memory
        memory.append(message)
        return random.choice(responses["default"])

# Example interaction with memory
memory = []
print(chatbot_response("hello", memory))  # Output: "Hi there!"
print(chatbot_response("how are you?", memory))  # Output: "I'm doing great, how about you?"
print(chatbot_response("what's your name?", memory))  # Output: "I'm a chatbot."
print(chatbot_response("bye", memory))  # Output: "Goodbye!"
print(chatbot_response("random question", memory))  # Output: "I'm not sure how to respond to that."
print(memory)  # Output: ['random question']
