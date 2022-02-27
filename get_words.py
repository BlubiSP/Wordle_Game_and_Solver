import requests

r = requests.get("https://rhdzmota.com/files/wordle.json", json=True)
words_list = (r.json())
with open("list.txt", "w") as file:
    words_string = "\n".join(words_list)
    file.write(words_string)