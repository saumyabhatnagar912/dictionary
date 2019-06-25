import json

data = json.load(open("data.json"))

query = input("Enter a word: ")
query = query.lower()
def find_meaning(w):
    try:
        return data[w]
    except:
        return "Word does not exist"
print(find_meaning(query))
