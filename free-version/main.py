# Dependency: https://github.com/xtekky/gpt4free
import g4f
import pyttsx3
from pynput import keyboard
import time
import random
import re

g4f.logging = True
g4f.check_version = False
print(g4f.version)
print(g4f.Provider.Ails.params)

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', vTEXT, flags=re.MULTILINE)
    return(vTEXT)

system_instructions = " Keep your answer to no more than 50 words."

prompts = [
    "Tell me a story with less than 50 words.",
    "Give me an idea for a stunt that I could do to become viral.",
    "Give me an idea for promoting my app.",
    "Give me a solution for poverty.",
    "Pick a debate topic and make an argument for both sides.",
    "Tell me a story in less than 50 words.",
    "Give me a random tip about how to overcome a productivity block.",
    "Tell me a random historical fact.",
    "Tell me a random fact about computer science.",
    "Give me a random tip about how to overcome a creative block.",
    "Tell me a joke.",
    "Tell me something amazing that someone did to become successful.",
    "Tell me how to embrace acceptance and gratitude.",
    "Tell me how to to deal with bad clients.",
    "Give me an example of something that requires balance between two opposing views.",
    "Tell me how to deal with mental health issues.",
    "Give me an idea for groundbreaking research.",
    "Tell me how to become a better leader.",
    "Tell me how to deal with stress and pressure at work.",
    "Tell me how to deal with boredom.",
    "Tell me how do I become better at my job as a web developer.",
    "Explain to me a random philosophy topic.",
    "Tell me a random historical fact about retro computers and video-games.",
    "Give me a random tip to manage my money better.",
    "Tell me one of the challenges behind selling software.",
    "Give me a reason why happiness is more important than money.",
    "Tell me a random fact about programming design patterns."
]

break_program = False
def on_press(key):
    global break_program
    if key.char == 'q':
        print ('Quit.')
        break_program = True
        return False
    
with keyboard.Listener(on_press=on_press) as listener:
    engine = pyttsx3.init()
    
    count = 0
    for i in range(1000):
        random.shuffle(prompts)
        for prompt in prompts:
            count += 1
            print(prompt)

            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                  {"role": "user", "content": prompt + system_instructions}
                ],
            )

            response = remove_urls(response)

            print(response)

            engine.say(response)
            engine.runAndWait()
            time.sleep(15)
            if break_program == True:
                quit()
    listener.join()


