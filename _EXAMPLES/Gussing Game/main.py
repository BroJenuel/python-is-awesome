import random

score = 3
randomNumber = random.randint(1, 10)


while True:
    if score == 0:
        print("Game Over!")
        break

    userNumberInput = int(input("Guess The Number from 1 to 10: "))

    if userNumberInput == randomNumber:
        print("Congratulations You Guessed it right! your score is: "+str(score))
        break
    else:
        print("Oops! Wrong: ")
        score -= 1
