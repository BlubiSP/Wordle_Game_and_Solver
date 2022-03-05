from functions import valid_guess


def main():
    print("Loading...")
    import functions, get_words, ui_prompts
    answer = functions.get_answer()
    functions.create_answer_file(answer)
    iW = "\n"
    niW = "\n"
    output = "_ _ _ _ _"
    print("Finished Loading")
    print("Starting Game!")
    guess = ui_prompts.get_guess()
    while not functions.solved(guess, answer):

        if functions.valid_guess(guess):
            correctPosition = functions.evaluate(guess, answer)["correctPosition"]
            inWord = functions.evaluate(guess, answer)["inWord"]
            notinWord = functions.evaluate(guess, answer)["notinWord"]

            if len(correctPosition) != 0:
                for f in correctPosition:
                    output = functions.output(output, f.letter, f.position)

            if len(inWord) != 0:
                list(set(inWord))
                for f in inWord:
                    if f.letter not in iW:
                        iW = iW + f.letter + " "
            
            if len(notinWord) != 0:
                list(set(notinWord))
                for f in notinWord:
                    if f not in niW:
                        niW = niW + f + " "

        print(output)
        if len(iW) > 1:
            print(functions.output2(iW, True))
        if len(niW) > 1:
            print(functions.output2(niW))
        guess = ui_prompts.get_guess()
    functions.delete_answer_file()
    print(f"The Word was {answer}! YOU WON")





if __name__ == "__main__":
    main()