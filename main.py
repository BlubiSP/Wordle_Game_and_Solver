from functions import valid_guess


def main():
    print("Loading...")
    import functions, get_words, ui_prompts
    answer = functions.get_answer()
    print("Finished Loading")
    print("Starting Game!")
    guess = ui_prompts.get_guess()
    while not functions.solved(guess, answer):
        print(answer)
        if functions.valid_guess(guess):
            correctPosition = functions.evaluate(guess, answer)["correctPosition"]
            inWord = functions.evaluate(guess, answer)["inWord"]
            if len(inWord) != 0:
                print(f"The following letters Were in the word:")
                for f in inWord:
                    print(f.letter)
            if len(correctPosition) != 0:
                print(f"The following letters Were in the correct Position:")
                for f in correctPosition:
                    print(f.letter)
        guess = ui_prompts.get_guess()
    print("You won xD")





if __name__ == "__main__":
    main()