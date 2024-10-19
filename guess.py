import random
guess = True 

while guess:
    scoreCount = 0 
    myNum = random.randint(1,100)
    guess2 = True 

    while guess2: 
                guess = input("Guess a number between 1 to 100: \n")
                scoreCount += 1
                while not guess.isdecimal():
                    print("Please enter a valid number: ")  
                    guess = input("Guess a valid number please: \n")   #asks for user to enter a number
                guess = int(guess)  #input is converted to integer

                if guess < myNum:   #checks if the guessed number is lower
                    print("Guess is lower than the actual number.")
                elif guess > myNum: #checks if the guessed number is higher
                    print("Guess is higher than the actual number.")
                else:
                    print(f"Great you guessed it correct!!!!")
                    finalscore = 10 - scoreCount
                    print(f"Your score is {finalscore}")    #counts the score
                    guess2 = False 
    playAgain = input("Do you want to play this again? Type 'Yes' if you want: \n")
    if playAgain.lower() == "yes":  #if the user enters yes, then the game starts again
                    guess = True
    else: 
        print("Thank you for playing!!!")
        guess = False   #if anything other than yes, the game doesn't continue

