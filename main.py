
def madlib():
    print("Welcome to MadLibs")
    noun = user_input("Enter a noun ")
    verb = user_input("Enter a verb ")
    adverb = user_input("Enter an adverb ")
    adjective = user_input("Enter an adjective ")
    print("This weekend I saw a " + noun + verb + "that was " + adverb + " " + adjective + ".")

def user_input(prompt):
    user_input = input(prompt)
    return user_input


madlib()
