def run_agent(messages):
    """
    Simple chatbot logic:
    - Echo user messages with basic responses
    """
    last_message = messages[-1].lower()
    
    if "hello" in last_message:
        return "Hi there! How can I help you?"
    elif "how are you" in last_message:
        return "I'm a bot, but I'm doing great!"
    elif "bye" in last_message:
        return "Goodbye! Have a nice day."
    else:
        return f"You said: {messages[-1]}"
