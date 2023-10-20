import openai
import pyttsx3
from pynput import keyboard
import time
import random
openai.api_key = ""

prompts = [
    "Tell me a story with less than 50 words.",
    "Tell me a recipe for pasta."
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

            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "user", "content": prompt}
              ]
            )

            answer = completion.choices[0].message.content
            print(answer)

            engine.say(answer)
            engine.runAndWait()
            time.sleep(1)
            if break_program == True:
                quit()
    listener.join()


