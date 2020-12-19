import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif word.upper() in data:
    return data[word.upper()]  
  elif len(get_close_matches(word,data.keys())) > 0:
    condition = input("Did you mean %s instead? Enter 'Y' or 'y' if yes or 'N' or 'n' if no: " % get_close_matches(word,data.keys())[0])
    if condition == 'Y' or condition == 'y':
      return data[get_close_matches(word,data.keys())[0]]
    elif condition == 'N' or condition == 'n':
      return "Please double check your input"  
    else:
      return "Invalid option! Try again."
    
  else:
    return "The word doesn't exist. Please check it." 

word = input("enter word: ")

output = translate(word)

if type(output) == list:
  for item in output:
    print(item)

else:
  print(output)