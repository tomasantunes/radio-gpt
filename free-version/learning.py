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

system_instructions = ""

prompts = [
    "Come up with a random math exercise and then go through the solution step by step.",
    "Come up with a random physics exercise and then go through the solution step by step.",
    "Come up with a random history question that could come up in a test and then give me and answer and justify.",
    "Come up with a random question that could come up in a computer science test and then give me an answer and justify.",
    "Come up with a random philosophy question that could come up in a test and then give me an answer and justify.",
    "Come up with a random question or exercise that could come up in a biology test and then give me an answer",
    "Come up with a random question that could could come up in an engineering quiz and then give me an answer",
    "Explain to me a random mathematical proof",
    "Explain to me a random concept of discrete math."
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
            response = response.replace("*", "")
            response = response.replace("#", "")

            print(response)

            engine.say(response)
            engine.runAndWait()
            time.sleep(15)
            if break_program == True:
                quit()
    listener.join()


