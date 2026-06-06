# Project KOKI — Day 2
# Dictionary brain + session memory
   #random isiliye use kra taki thoda robotic feel na aaye....
import random

responses = { #bahut se random responses daal diye ab ek word pr iske pass 3 alag alag response ho skte hai for exam hello type krne pr hi there bhi aa skta hai aur kya haal hai bhi...{aage dikkat nhi aani chahiye}
    "hello": ["Hey! Good to see you.", "Hello! Kya haal hai?", "Hi there!"],
    "how are you": ["Getting smarter every day!", "Learning and growing!"],
    "motivate me": ["Har mushkil ek naya lesson hai.", "Tu kar sakta hai bhai.", "Keep going. KOKI believes in you."],
    "good morning": ["Good morning! Aaj bhi ek naya chance hai."],
    "good night": ["Good night! Kal phir milte hain."],
    "joke": ["Why do programmers prefer dark mode? Because light attracts bugs!"],
    "army": ["Indian Army — ek legacy, ek commitment. Jai Hind."],
    "koki": ["Haan bhai, main hoon. KOKI. Tera apna AI."],
    "bye": ["Goodbye! See you tomorrow."]
}

conversation_count = 0
        # def function iska response decide krega based on use input
def greet():
    name = input("KOKI: What's your name? ")
    print("KOKI: Hello " + name + "! I am KOKI. Still learning, but I'm here.")
    return name

def listen():
    return input("You: ")

def respond(msg, name):
    global conversation_count
    conversation_count += 1
    #matching ke liye use kra lower case ka taki Hello ya Fir hello same lage
    msg = msg.lower().strip()
    
    for key in responses:
        if key in msg:
            reply = random.choice(responses[key])
            print("KOKI: " + reply)
            if conversation_count == 5:
                print("KOKI: 5 messages already " + name + ". I like talking to you.")
            return True
    
    print("KOKI: Still learning " + name + ". I don't know this yet.")
    return True

# Start
name = greet()
running = True
while running:
    msg = listen()
    if "bye" in msg.lower():
        print("KOKI: Goodbye " + name + ". See you tomorrow.")
        running = False
    else:
        respond(msg, name)