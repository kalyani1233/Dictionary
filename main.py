import json
import art
from colorama import *
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
    elif word.capitalize() in data:
        return  data[word.capitalize()]
    elif len(get_close_matches(word,data.keys()))>0:
        print(Fore.GREEN,"Did  u want {} instead ".format(get_close_matches(word ,data.keys())[0])) # not all words only single word
        decide = input("if this is a correct match enter yes/no yes->y no->n")
        if decide=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif decide =='n':
            return "Word does not exits"



    else:
        print(Fore.RED,"word not found!!!")




while(True):
    print(Fore.GREEN)
    word=input("Enter the word you want search!!")
    output= translate(word) #data[word]
    print(output)
    print(Fore.YELLOW)
    con = input("Did you want to continue searching yes/no.....")
    if con == "no" or con=="No":
        break
