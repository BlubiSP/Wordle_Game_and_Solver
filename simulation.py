def main():
    
    import functions, random, cheats, time

    num_of_simulation = input("Enter number of simulations:\n")
    guess = input("Enter guess ( has to be 5 letters)\n")
    if len(guess) != 5 or not guess.isalpha():
        raise ValueError("Invalid guess\n")


    possible_answers = functions.read_list("answers.txt")
    #starting guess
    
    
    def guessing(list_of_possible_answers, guess, answer):
        new_list_of_answers = cheats.get_list_of_possible_answers(functions.evaluate(guess, answer), list_of_possible_answers)
        guess = random.choice(new_list_of_answers)
        return (new_list_of_answers, guess)

    def game(guess, possible_answers, answer):
        num_of_tries = 0
        while guess != answer:
            possible_answers, guess = guessing(possible_answers, guess, answer)
            num_of_tries += 1 

        return (num_of_tries, answer)

    total = 0
    lost = 0
    lose_words = []
    for n in range(int(num_of_simulation)):
        # data = [number of tries, answer]
        answer = random.choice(possible_answers)
        data = game(guess, possible_answers, answer)
        # Lose if you it needs more than 6 guesses
        if data[0] > 6:
            lost += 1
            print(f"LOST")
            lose_words.append(data[1])

        else:
            total += data[0]

        print(f"Finished game {n} of {num_of_simulation}")

    print(f"Average guesses to win: {total / int(num_of_simulation)}\nGames lost: {lost}")
    if lose_words:
        print("\nCould not guess:")
        for l in lose_words:
            print(l)
    input()

if __name__ == "__main__":
    main()