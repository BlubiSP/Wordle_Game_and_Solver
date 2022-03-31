def main():
    import functions, random, cheats, time
    num_of_simulation = input("Enter number of simulations:\n")
    guess = input("Enter guess ( has to be 5 letters")
    if len(guess) != 5 or not guess.isalpha():
        raise ValueError("Invalid guess. Exiting program")
        time.sleep(3)
        exit()
    possible_answers = functions.read_list("answers.txt")
    #starting guess
    guess = "crane"
    answer = random.choice(possible_answers)

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
    for _ in range(int(num_of_simulation)):
        # data = [number of tries, answer]
        data = game(guess, possible_answers, answer)
        # If the programm needs more then 6 tries it will print the last guess and the answer here
        # I simulated 10k games and it could not loose
        if data[0] > 6:
            lost += 1
            print(f"Number of Guesses = {data[0]}\nAnswer = {data[1]}")

        else:
            total += data[0]

    print(f"Average guesses to win: {total / int(num_of_simulation)}\nGames lost: {lost}")


if __name__ == "__main__":
    main()