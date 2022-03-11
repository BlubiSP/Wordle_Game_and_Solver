
def main():
    import requests
    r = requests.get("https://rhdzmota.com/files/wordle.json", json=True)
    words_list = (r.json())
    with open("list_of_valid_guesses.txt", "w") as file:
        words_string = "\n".join(words_list)
        file.write(words_string)


if __name__ == "__main__":
    main()