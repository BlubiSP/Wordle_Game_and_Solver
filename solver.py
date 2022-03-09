# keep old input
# fix finish
def main():
    print("Loading...")
    import cheats, functions, random
    possible_answers = functions.read_list("answers.txt")

    guess = "crane"
    def get_guess():
        inWord = []
        correctPosition = []
        notinWord = []
        returndic = {}
        print("Press enter when you are done")
        _ = input()
        print("Any correct Letters AND correct position? (GREEN)")
        print("Enter them in this format:")
        print("(letter position, letter position) Example: a1, p2, p3, l4, e5")
        print("If there are none just press enter.")
        correctletterandposition = input()
        if len(correctletterandposition) > 0:
            correctPosition = functions.conv_into_class(correctletterandposition)
        print("Any correct Letters? (ORANGE)")
        print("Enter them in this format:")
        print("(letter position, letter position) Example: a1, p2, p3, l4, e5")
        print("If there are none just press enter.")
        correctletter = input()
        if len(correctletter) > 0:
            inWord = functions.conv_into_class(correctletter)
        print("Any incorrect Letters? (GREY)")
        print("Enter them in this format:")
        print("(letter, letter) Example: a, p, p, l, e")
        print("If there are none just press enter.")
        incorrectLetters = input()
        if len(incorrectLetters) > 0:
            notinWord = incorrectLetters.replace(" ", "").split(",")
        returndic["inWord"] = inWord
        returndic["correctPosition"] = correctPosition
        returndic["notinWord"] = notinWord
        list_of_possible_answers = cheats.get_list_of_possible_answers(returndic, possible_answers)
        return list_of_possible_answers

    print("Finished Loading")
    while isinstance(guess, str) or len(guess) != 1:
        if isinstance(guess, str):
            print(f"Guess {guess}!")
        else:
            print(f"Guess {random.choice(guess)}!")
        guess = get_guess()
    print(f"The answer is {guess}")
    
    

if __name__ == "__main__":
    main()
