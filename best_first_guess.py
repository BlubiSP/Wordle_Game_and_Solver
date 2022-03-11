#Incomplete
#needs threading otherwise it will take weeks to complete

import cheats, functions
valid_words = functions.read_list("list_of_valid_guesses.txt")
possible_answers = functions.read_list("answers.txt")

def best_first_guess(valid_words = valid_words, possible_answers = possible_answers):
    shortest = [1000, "none"]
    total = 0
    shortest2 = [1000, "none"]
    for n, f in enumerate(valid_words):
        for i in possible_answers:
            total += len(cheats.get_list_of_possible_answers(functions.evaluate(f, i), possible_answers))
        average = total / len(possible_answers)
        if average < shortest[0]:
            shortest = [average, f]
            
        total = 0
        print(f"{n}/{len(valid_words)}")
    print(shortest)


best_first_guess()