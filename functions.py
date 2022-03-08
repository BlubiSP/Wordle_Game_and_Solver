import random
import os


def read_list(filename):
    with open(filename, "r") as file:
        words_string = file.read()
        words_list = words_string.split("\n")
    return words_list

words_list = read_list("list.txt")
answer_list = read_list("answers.txt")

def get_answer(answers = answer_list):
    return random.choice(answers)

def valid_guess(guess, words_list = words_list):
    if guess.lower() in words_list:
        return True

    print("Invalid guess. Try Again!")

def solved(guess,answer):
    if guess.lower() == answer.lower():
        return True

    return False

def evaluate(guess, answer):
    
    class CorrectLetters:
        def __init__(self, letter, position=None):
            self.letter = letter
            self.position = position

    inWord = []
    correctPosition = []
    notinWord = []
    returndic = {}
    double = False
    #print(f"Guessed {guess}")
    for n, i in enumerate(guess):
        if i in answer:
            if answer[n] == i:
                i = CorrectLetters(i, n)
                correctPosition.append(i)

            else:
                #
                i = CorrectLetters(i, n)
                #
                for c in inWord:
                    double = False
                    if c.letter == i.letter:
                        double = True
                        break
                if not double:
                    inWord.append(i)
        else:
            notinWord.append(i)
    #print(f"Answer is {answer}")
    #if len(inWord) > 0 :
    returndic["inWord"] = inWord

    #if len(correctPosition) > 0 :
    returndic["correctPosition"] = correctPosition

    #if len(notinWord) > 0 :
    returndic["notinWord"] = notinWord
    return returndic

def output(display, letter, position):
    return display[:position * 2] + letter + display[position * 2 + 1:]

def output2(dynamic, inword = False):
    if inword:
        return f"The following letters were in the word:\n{' '.join(sorted(dynamic)).strip()}"
    else:   
        return f"The following letters were NOT in the word:\n{' '.join(sorted(dynamic)).strip()}"    
    
def create_answer_file(answer):
    with open("answer.txt", "w") as file:
        file.write(answer)

def delete_answer_file():
    os.remove("answer.txt")