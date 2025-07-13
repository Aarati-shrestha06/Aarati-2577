import random

print("\t\tWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")


secret_number=random.randint(1,100)

while True:
    guessed_number=int(input("Enter your guess : "))


    if guessed_number==secret_number:
        print("\tCongratulation ! \n")
        print("You got it!")
        break   

    elif guessed_number < secret_number:
        print("Your guess number is low! \"Try Again\"") 
        
    





