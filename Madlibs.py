# def mablibs(name, adjective, food_plural, noun_plural, verb_ending_ed,):


# print("Welcome to my MadLib program. Please enter some information below:")

# return ""


# name: Starr
# adjective: huge
# noun: tablecloth
# adjective: dry
# food_plural: tacos
# noun_plural: packs
# verb_ending_ed: ended
# noun: jellyfish

# noun = input("What is your noun?")
# print(noun)

# verb = input("What is your verb?")
# print(verb)

# adjective = input("What is your adjective?")
# print(adjective)
from collections import defaultdict
from json import dumps

def gatherUserInput():
    noun = input("What is your noun?")
    verb = input("What is your verb?")
    adjective = input("What is your adjective?")
    adverb = input("What is your adverb?")

    user_inputs = defaultdict(list)
    user_inputs['nouns'].append(noun)
    user_inputs['verbs'].append(verb)
    user_inputs['adjs'].append(adjective)
    user_inputs['adv'].append(adverb)
    print(dumps(user_inputs))
    return user_inputs

gatherUserInput()
