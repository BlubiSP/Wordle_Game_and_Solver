# It's not perfect. It does not account for duplicate letters
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
        _ = input("Press enter when you are done\n")

        print("Any correct Letters AND correct position? (GREEN)")
        print("Enter them in this format:")
        print("(letter position, letter position) Example: a1, p2, p3, l4, e5")
        
        correctletterandposition = input("If there are none just press enter.\n").strip(",")
        if len(correctletterandposition) > 0:
            try:
                correctPosition = functions.conv_into_class(correctletterandposition)
           
            except ValueError:
                print("ERROR: Invalid input\nIgnoring input.")

        print("Any correct Letters? (ORANGE)")
        print("Enter them in this format:")
        print("(letter position, letter position) Example: a1, p2, p3, l4, e5")
        
        correctletter = input("If there are none just press enter.\n").strip(",")
        if len(correctletter) > 0:
            try:
                inWord = functions.conv_into_class(correctletter)

            except ValueError:
                print("ERROR: Invalid input\nIgnoring input.")

        print("Any incorrect Letters? (GREY)")
        print("Enter them in this format:")
        print("(letter, letter) Example: a, p, p, l, e")
        
        incorrectLetters = input("If there are none just press enter.\n").strip(",")
        if len(incorrectLetters) > 0:
            try:
                notinWord = incorrectLetters.replace(" ", "").split(",")

            except ValueError:
                print("ERROR: Invalid input\nIgnoring input.")
        # converting inputs into A dictionary
        returndic["inWord"] = inWord
        returndic["correctPosition"] = correctPosition
        returndic["notinWord"] = notinWord
        list_of_possible_answers = cheats.get_list_of_possible_answers(returndic, possible_answers)
        
        return list_of_possible_answers

    print("Finished Loading")

    while len(guess) != 1:

        if isinstance(guess, str):
            print(f"Guess {guess}!")

        else:
            if len(guess) == 0:
                print("ERROR: 0 Possible answers.\nYou made a wrong input. Try again!")
                quit()
                
            else:
                print(f"Possible Answers:\n{guess}")
                print(f"Guess {random.choice(guess)}!")

        guess = get_guess()
    
    print(f"The answer is {guess[0]}!")
    input()

if __name__ == "__main__":
    main()