import random
import sys
def guess_the_number(end_val):
    choice=input("Hello, Gamer ! Do you wanna play this awesome number guessing game ? enter Y for YES and N for NO >> ")
    choice=choice.lower()
    if choice=="y":
        print("Welcome")
        val=0
        correct_val=random.randint(1,end_val)
        print(f"Guess the number between 1 to {end_val} >> ")
        while val!=correct_val:
            val=int(input())
            if val>correct_val:
                print("To High Guess again...")
            elif val<correct_val:
                print("To Low Guess again...")
        print(f"Congrats You Guessed The Correct Number Which is {correct_val}")

    else:
        sys.exit()   
end_val=random.randint(1,50)
guess_the_number(end_val)
