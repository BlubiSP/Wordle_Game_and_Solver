def main():
    import functions, random, cheats
    num_of_simulation = input("Enter number of simulations:\n")
    possible_answers = functions.read_list("answers.txt")
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
        return (num_of_tries, guess, answer)
    total = 0
    lost = 0
    for _ in range(int(num_of_simulation)):
        tries = game(guess, possible_answers, answer)[0]
        if tries > 6:
            lost += 1
            print(f"guess = {tries[1]}\nAnswer = {tries[2]}")
        else:
            total += tries
    print(f"Average guesses to win: {total / int(num_of_simulation)}\nGames lost: {lost}")
if __name__ == "__main__":
    main()

