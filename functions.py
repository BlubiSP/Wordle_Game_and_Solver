import random


def read_list():
    with open("list.txt", "r") as file:
        words_string = file.read()
        words_list = words_string.split("\n")
    return words_list

words_list = read_list()

def get_answer(words_list = words_list):
    return random.choice(words_list)

def valid_guess(guess, words_list = words_list):
    if guess.lower() in words_list:
        return True

    print("Invalid guess. Try Again!")

def solved(guess,answer):
    if guess.lower() == answer:
        return True

    return False

def evaluate(guess, answer):
    
    class CorrectLetters:
        def __init__(self, isinAnswer, letter=None, position=None):
            self.isinAnswer = isinAnswer
            self.letter = letter
            self.position = position

    inWord = []
    correctPosition = []

    for n, i in enumerate(guess):
        if i in answer:
            if answer[n] == i:
                i = CorrectLetters(True, i, n)
                correctPosition.append(i)

            else:
                i = CorrectLetters(True, i)
                inWord.append(i)

    return {"correctPosition" : correctPosition, "inWord": inWord}