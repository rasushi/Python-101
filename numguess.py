import random

print("ITS ROULETTE TIMEEE!!!")
lb,ub=1,100
print("Player You get SIX chances to guess the correct number and win the lottery...\nYour guesses shoud be an INTEGER between 1 and 100...\nMay the force be with you")
number=random.randint(lb,ub)

for i in range (1,7,1):
    guess=int(input("Please enter your guess:"))
    if (number==guess):
        print(f"Odin's beard! you guessed it rightt.. \nThe number was {number} \ngo to 'https:\\lokis_treasures' to get your prize")
        break
    else:
        if(guess<number):
            print("Your guess is too low")
        else:
            print("Your guess is too high")
    print(f"You have {6-i} guesses left")    

print("OH NOOO! you ran out of guesses. Better luck next time..")  
