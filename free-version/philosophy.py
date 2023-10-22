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

instructions = "Tell me everything you know about the following topic. "
instructions_after = "Include explanations of sub-topics and examples. And tell me a bit about the history and impact on society."

prompts = [
    "The nature of reality",
    "The concept of free will",
    "Determinism versus indeterminism",
    "The philosophy of time",
    "The problem of universals",
    "The nature of objects and their properties",
    "Dualism versus monism",
    "The philosophy of space",
    "The concept of substance",
    "The problem of personal identity",
    "The nature of knowledge",
    "Skepticism and certainty",
    "The problem of induction",
    "Rationalism versus empiricism",
    "The theory of justification",
    "The Gettier problem",
    "The role of perception in knowledge",
    "The concept of belief",
    "The nature of truth",
    "The philosophy of language and meaning",
    "Utilitarianism",
    "Deontological ethics",
    "Virtue ethics",
    "The concept of moral responsibility",
    "The ethics of care",
    "The nature of good and evil",
    "The trolley problem",
    "The ethics of animal rights",
    "The problem of evil",
    "Bioethics and medical ethics",
    "The concept of justice",
    "The social contract",
    "Libertarianism versus socialism",
    "The philosophy of law",
    "Democracy and its critics",
    "The concept of rights",
    "The notion of freedom",
    "The role of the state",
    "The philosophy of education",
    "The ethics of war and peace",
    "The philosophy of art",
    "The concept of beauty",
    "The nature of aesthetic experience",
    "The philosophy of music",
    "The philosophy of literature",
    "The concept of taste",
    "The role of intention in art",
    "The nature of creativity",
    "The philosophy of film",
    "The aesthetics of nature",
    "Propositional logic",
    "Predicate logic",
    "The nature of argumentation",
    "Fallacies and argumentative errors",
    "The philosophy of mathematics",
    "The concept of proof",
    "The theory of inference",
    "The philosophy of science",
    "The problem of confirmation",
    "The philosophy of logic",
    "The nature of consciousness",
    "The problem of other minds",
    "The philosophy of perception",
    "Dualism versus physicalism",
    "The mind-body problem",
    "Artificial intelligence and consciousness",
    "The nature of emotions",
    "The philosophy of cognitive science",
    "The concept of intentionality",
    "The problem of qualia",
    "Arguments for the existence of God",
    "The problem of evil and suffering",
    "The nature of faith and reason",
    "The concept of the soul",
    "The philosophy of miracles",
    "The nature of religious experience",
    "Atheism and agnosticism",
    "The philosophy of death and afterlife",
    "The concept of karma and reincarnation",
    "The problem of religious pluralism",
    "The philosophy of existence",
    "The concept of authenticity",
    "The philosophy of freedom",
    "The nature of despair and suffering",
    "The philosophy of Jean-Paul Sartre",
    "The philosophy of Martin Heidegger",
    "The concept of the absurd",
    "The philosophy of phenomenology",
    "The philosophy of Edmund Husserl",
    "Existentialism and ethics",
    "The philosophy of technology",
    "The ethics of artificial intelligence",
    "The philosophy of language and linguistics",
    "Feminist philosophy",
    "The philosophy of race and ethnicity",
    "The philosophy of gender and sexuality",
    "Environmental philosophy",
    "The ethics of climate change",
    "The philosophy of mental health",
    "The philosophy of social media and the internet",
    "The Law Of Attraction",
    "Aristotelian Virtue Ethics",
    "Rousseau’s “The Social Contract”",
    "Karma",
    "The Socratic Method",
    "Nihilism",
    "Plato’s Allegory Of The Cave",
    "The Multiverse Theory",
    "Eternalism",
    "Plato’s Cave",
    "Solipsism",
    "The Big Freeze",
    "Religion",
    "Logic",
    "Feminist",
    "Education",
    "Law",
    "Romanticism",
    "Skepticism",
    "Ethics",
    "Natural",
    "Moral",
    "Metaphysical",
    "Language",
    "Mind",
    "Human Nature",
    "Metaphilosophy",
    "Idealism",
    "Presentism",
    "The Brain In A Jar",
    "Fictional Realism",
    "Confucianism",
    "I Think, Therefore I Am",
    "Samsara",
    "Platonism",
    "Sense Data",
    "Stoicism",
    "Consequentialism",
    "Deontology"
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
                  {"role": "user", "content": instructions + prompt + instructions_after}
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