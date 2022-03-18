import random
import os

class CorrectLetters:
        def __init__(self, letter, position=None):
            self.letter = letter
            self.position = position

def read_list(input, file=True):
    # gets real filepath
    real_path = os.path.realpath(__file__)
    real_path_without_current_file = real_path[:-real_path[::-1].find("\\")]
    #                                         (      find last "\"       )
    #reverse slashes
    real_path = ""
    for s in real_path_without_current_file:
        if s != "\\":
            real_path += s

        else:
            real_path += "/"
    
    #Reads text file and returns is as list
    if file:
        with open(real_path + input, "r") as file:
            words_string = file.read()
            words_list = words_string.split("\n")
    else:
        words_list = input.split("\n")
        
    return words_list

words_list = read_list("list_of_valid_guesses.txt")
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
    # compares guess to answer letter for letter
    # returning a dictionary
    ## Example: We know the letter in the second position is "a", there is no "w" or "r" and there is an "e" somewhere but not in position 3
    # {'inWord': [class with .letter e and .position3], 'correctPosition': [class with .letter a and .position 2], 'notinWord': ['w', "r"]}
    
    inWord = []
    correctPosition = []
    notinWord = []
    returndic = {}
    #
    double = False
    #
    for n, i in enumerate(guess):
        if i in answer:
            #if letter and position from guess match with answer
            if answer[n] == i:
                i = CorrectLetters(i, n)
                correctPosition.append(i)
            # if only the letter from the guess is in the answer
            
            else:
                i = CorrectLetters(i, n)
                inWord.append(i)
        
        else:
            notinWord.append(i)
    returndic["inWord"] = inWord
    returndic["correctPosition"] = correctPosition
    returndic["notinWord"] = notinWord
    return returndic

def output(display, letter, position):
    # have to do * 2 because of the spaces between the "_"
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

def conv_into_class(string):
    r = []
    if len(string) > 0:
        stripped_list = string.replace(" ", "").split(",")
        r = [CorrectLetters(f[0], int(f[1]) -1) for f in stripped_list]
    
    return r