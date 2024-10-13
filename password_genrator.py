from random import sample
import string

def pass_generator(length): # It's a function to generate random passwords for you

    lowerData = string.ascii_lowercase # It is store all the lower case values a to z
    upperData = string.ascii_uppercase # It is store all the upper case values A to Z
    digitsData = string.digits # It stores all the number 0 to 9
    symbolsData = string.punctuation # It stores all punctuation symbols

    combineData = lowerData + upperData + digitsData + symbolsData # It combines all above data
    pass_gen = sample(combineData, length) # It is a random module function that takes data and length and generate a password
    password = "".join(pass_gen) # .join() combine the above data with empty string or without space
    print(f"You password is = {password}")
    return password


if __name__ == "__main__":
    print("\n___________Welcome to our Password Generator____________\n")

    while True:
        length = int(input("\nEnter the lenght of the password you want to generate: "))
        pass_generator(length)

        choice = input("\nDo you want to generate another password:(yes/no) ").strip().lower()
        if choice == "no":
            print("Password Generator is quiting...........\n")
            break