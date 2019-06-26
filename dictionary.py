import json
from difflib import get_close_matches

data = json.load(open("data.json"))

query = input("Enter a word: ")

def find_meaning(w):
    if w in data:
        return data[w]
    elif w.lower() in data:
        return data[w.lower()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        print("Did you mean %s?" %get_close_matches(w,data.keys())[0])
        user_input = input("Type Y for yes, N for no: ")
        if user_input == "Y" or user_input =="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif user_input == "N" or user_input =="n":
            return "%s word does not exist" %w
        else:
            return "We do not understand your entry, try again!"
    else:
        return "%s word does not exist" %w

output = find_meaning(query)

if type(output) is list:
    for o in output:
        print(o)
else:
    print(output)
