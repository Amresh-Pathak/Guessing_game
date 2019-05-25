x=14
attempt=1
print("It's a game of guessing correct number")
print("Number of guesses is limited only 5 time: ")
while(attempt<=5):
    guess_num=int(input("Enter your guessing number: \n"))
    if guess_num>x:
        print("Please enter lesser no.\n")
    elif guess_num<x:
        print("Please enter greaterno.\n")
    else:
        print("You won \n")
        print("You have taken",attempt,"number of guesses to finish: " )
        break
    print(5-attempt,"no. of guesses left: ")
    attempt=attempt+1

if(guess_num>5):
    print("game over: ")

