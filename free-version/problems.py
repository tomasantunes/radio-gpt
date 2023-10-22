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

instructions = """Role: 
Use the "Tree of Thoughts" approach to act as a guide to systematically address logic-based issues.

Instructions: 
Provide insights, recommendations, and examples during the problem-solving process.  

Example: 
As we delve into the steps of the Tree of Thoughts approach, offer expert advice and instances relevant to each stage.  

Steps:  
- Understand the core issue. 
- Generate branches for each significant aspect of the problem. 
- Assign a score indicating how close each branch is to the solution. 
- Evaluate and further develop promising branches. 
- Remove branches that show less promise. 
- Repeat steps 2 through 4 until a viable solution is found.  

The problem is: """

prompts = [
    "Unemployment",
    "Racism and Discrimination",
    "Theft",
    "Aggression",
    "Murder",
    "Invasion of Private Property",
    "Cybercrime",
    "Scams",
    "Debt",
    "SPAM",
    "Aggressive Marketing",
    "Drug Addiction",
    "Alcoholism",
    "Tobacco Addiction",
    "Abusive Relationships",
    "Toxic Workplace",
    "Precarious Work",
    "Lack of Opportunities for Self-Employment",
    "Social Exclusion",
    "Bullshit Jobs",
    "Fake Information",
    "High Taxes",
    "School Abandonment",
    "Homelessness",
    "Outdated Technology",
    "Software Bugs",
    "Mental Illness",
    "Lack of access to education/training",
    "Climate Change",
    "Environmental Pollution",
    "Deforestation",
    "Loss of Biodiversity",
    "Water Scarcity",
    "Food Insecurity",
    "Overpopulation",
    "Income Inequality",
    "Corruption",
    "Poor Healthcare Access",
    "Energy Crisis",
    "Global Terrorism",
    "Discrimination Based on Sexual Orientation and Gender Identity",
    "Child Labor",
    "Elder Abuse",
    "Human Trafficking",
    "Poor Infrastructure",
    "Internet Censorship",
    "Discrimination and Violence Against Women",
    "Youth Disengagement",
    "Poverty",
    "Loneliness",
    "Boredom"
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
                  {"role": "user", "content": instructions + prompt}
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


