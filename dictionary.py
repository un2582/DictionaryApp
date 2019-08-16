import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    else:
        #are there any close matches? if so, pull out the 1st one
        if len(get_close_matches(word,data.keys())) > 0:
            recc_word = get_close_matches(word,data.keys())[0]
            answer = input("Did you mean {}? Press Y or N: ".format(recc_word))
            if answer == "Y" or answer == "y":
                return data[recc_word]
            else:
                return "You've answered No"
        else:
            return "There were no words close to that found"

while(True):
    word = input("Please input a word: ")
    if word == "Q" or word == "q":
        print("You've chosen to quit")
    else:
        print(translate(word))
