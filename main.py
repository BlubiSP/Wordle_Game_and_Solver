from functions import valid_guess


def main():
    print("Loading...")
    import functions, get_words, ui_prompts
    answer = functions.get_answer()
    functions.create_answer_file(answer)
    output = "_ _ _ _ _"
    print("Finished Loading")
    print("Starting Game!")
    guess = ui_prompts.get_guess()
    while not functions.solved(guess, answer):

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
                    output = functions.output(output, f.letter, f.position)

        print(output)
        guess = ui_prompts.get_guess()
    try:
        functions.delete_answer_file()
    except any:
        pass
    print(f"The Word was {answer}! YOU WON")





if __name__ == "__main__":
    main()