import random
import Art
print(Art.logo)
#get a magic number to guess using random module
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
magic=random.randrange(1,100)

level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if level=='easy':
    no_of_guesses=10
elif level=='hard':
    no_of_guesses=5
else:
    print("Invalid input!")

i=0
while i<no_of_guesses:
    print(f"You have {no_of_guesses} attempts remaining to guess the number.")
    your_guess=int(input("Make a guess: "))
    if your_guess<magic:
        print("Too Low⬇️")
        print("Try Again🙁")
        no_of_guesses-=1
    elif your_guess>magic:
        print("Too High⬆️")
        print("Try Again🙁")
        no_of_guesses-=1
    elif your_guess==magic:
        print(f"You got it! the answer was {magic}🥳")
        break