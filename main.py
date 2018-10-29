
def madlib_go():
    print("Welcome to MadLibs")
    print("Please read the the paragraph below and then fill in the prompts to complete the spooky Halloween story!")
    print("Happy Halloween! It’s time to get (emphasis adjective) spooky. Get your (article of clothing) on and prepare to (verb) around the town. Every year on October 31st, (fictional city) hosts the (adjective) party and (plural proper noun) never forget to come. It is important to greet everyone by saying “ (noun) or (noun) “. We will eat lots of (food) and drink (beverage). Bring your finest (adjective) (noun) and don’t forget to (verb) because this is the most (adjective) day of the year. ")
    emphasis_adjective = user_input("Enter an emphasis adjective: ")
    article_of_clothing = user_input("Enter an article of clothing: ")
    verb_one = user_input("Enter a verb: ")
    fictional_city = user_input("Enter a fictional city: ")
    adjective_one = user_input("Enter an adjective: ")
    plural_proper_noun = user_input("Enter a plural proper noun:  ")
    noun_one = user_input("Enter a verb: ")
    noun_two = user_input("Enter a noun:  ")
    food = user_input("Enter a food: ")
    beverage = user_input("Enter a beverage: ")
    adjective_two = user_input("Enter an adjective: ")
    noun_three = user_input("Enter a noun: ")
    verb_two = user_input("Enter a verb: ")
    adjective_three = user_input("Enter an adjective: ")
    print("Happy Halloween! It’s time to get " + emphasis_adjective + " spooky. Get your " + article_of_clothing + " on and prepare to " + verb_one + " around the town. Every year on October 31st, " + fictional_city + " hosts the " + adjective_one + " party and " + plural_proper_noun + " never forget to come. It is important to greet everyone by saying ‘ " + noun_one + " or " + noun_two + " .’ We will eat lots of " + food + " and drink " + beverage + " . Bring your finest " + adjective_two + noun_three + " and don’t forget to " + verb_two + " because this is the most " + adjective_three + " day of the year.")

def user_input(prompt):
    user_input = input(prompt)
    return user_input


madlib_go()
