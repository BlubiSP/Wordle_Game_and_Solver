import random 
import requests

r = requests.get("https://rhdzmota.com/files/wordle.json", json=True)
possible_words = (r.json())

def get_answer(possible_words = possible_words):
    return random.choice(possible_words)

print(get_answer())
