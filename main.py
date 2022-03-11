import cheats
def main():
    print("Loading...")
    import functions
    answer = functions.get_answer()
    functions.create_answer_file(answer)
    iW = "\n"
    niW = "\n"
    c = {'inWord': [], 'correctPosition': [], 'notinWord': []}
    output = "_ _ _ _ _"
    print("Finished Loading")
    print("Starting Game!")
    guess = input("Enter Guess...\n")

    ### Cheats
    #answer_list = functions.read_list("answers.txt")
    ###

    while not functions.solved(guess, answer):
        if functions.valid_guess(guess):
            inWord, correctPosition, notinWord = functions.evaluate(guess, answer).values()

            if len(correctPosition) != 0:
                for f in correctPosition:
                    output = functions.output(output, f.letter, f.position)

            if len(inWord) != 0:
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

        ### Cheats
        #answer_list = cheats.get_list_of_possible_answers(functions.evaluate(guess, answer), answer_list)
        #print(answer_list)
        ###

        guess = input("Enter Guess...\n")

    functions.delete_answer_file()
    print(f"The Word was {answer}! YOU WON")





if __name__ == "__main__":
    main()