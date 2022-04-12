import json


def get_word_definition(word):
    with open("data.json") as j_data:
        data = json.load(j_data)
    if word in data:
        searched_word = "\n".join(data[word])
        return f"\n{word}:\n{searched_word}"
    else:
        return f"Sorry, {word} can't be found in our dictionary."
