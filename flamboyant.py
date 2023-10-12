import random

def tell_me_a_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why was the math book sad? Because it had too many problems.",
        "How does a penguin build its house? Igloos it together!",
    ]
    
    return random.choice(jokes)

print(tell_me_a_joke())
