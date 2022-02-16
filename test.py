import random 
import requests

r = requests.get("https://rhdzmota.com/files/wordle.json", json=True)
words_list = (r.json())

def get_answer(words_list = words_list):
    return random.choice(words_list)

def valid_guess(guess, words_list = words_list):
    if guess.lower() in words_list:
        return True
    return False


print(valid_guess("clane"))