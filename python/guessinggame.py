import random

print("\t\tWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Try to guess it!")


secret_number=random.randint(1,10)

i = 0

while i<3:
    guessed_number=int(input("Enter your guess : "))


    if guessed_number==secret_number:
        print("\tCongratulation ! \n")
        print("You got it!")
        break

    elif guessed_number < secret_number:
        print("Your guess number is low! \"Try Again\"") 
    
    else:
        print("Your guess number is high! \"Try Again\"")

    i+=1

print(f"the secret number was {secret_number}")


        
    





