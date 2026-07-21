
"""
Project 1: Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - Batch 2026
"""

#  Knowledge Base (Intents) 
responses = {
    'hello': 'Hi there! How can I help you today?',
    'hi': 'Hello! Nice to see you.',
    'how are you': '  I am doing great! How about you?',
    'what is your name': 'I am a rule-based chatbot .',
    'what can you do': 'I can respond to greetings and a few basic questions using simple rules.',
    'help': 'I am only able to answer few questions because i am Rule-Based Ai Chatbot .Thank You!!',
    'thank you': 'You are welcome!',
    'thanks': 'Anytime!',
}

#  Exit Commands 
exit_commands = {'exit', 'quit', 'bye', 'goodbye','by'}

#  Fallback Response 
DEFAULT_REPLY = "I do not understand. Could you rephrase that?"


def get_response(user_input: str) -> str:
    """Look up a reply for the cleaned user input, with a fallback."""
    return responses.get(user_input, DEFAULT_REPLY)


def run_chatbot():
    print("Chatbot: Hello! Type 'bye' or 'exit' to end the chat.\n")

    while True:
        raw_input_text = input("You: ")

        # Sanitization / Normalization
        clean_input = raw_input_text.lower().strip()

        # Exit condition (Kill Command)
        if clean_input in exit_commands:
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Process input and generate reply
        reply = get_response(clean_input)
        print(f"Chatbot: {reply}")


if __name__ == "__main__":
    run_chatbot()
