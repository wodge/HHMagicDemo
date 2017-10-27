import random
import time
import sys

print("\tAge Guesser!")
print("\t8 tries only!")
name = input("\nWhat's your name? ")


num = 80
min_num = 6
tries = 1

number = random.randint(min_num, num)

print("\nLet me guess... You are", number, "years old?")
guess = input("'Higher', 'Lower', or was it 'Correct'? ")
guess = guess.lower()

while guess != "correct":
    if tries == 8: #can be increased to reduce failure
        print("\n I guess I couldn't guess your age....")
        print("Closing...")
        time.sleep(5)
        sys.exit()
    elif guess == "higher":
        print("Let me think...")
        min_num = number + 1  #### Here is my trouble - Don't know how to limit max number
        time.sleep(3) # pause
    elif guess == "lower":
        print("Let me think...")
        num = number - 1
        time.sleep(3) # pause
    number = random.randint(min_num, num) #<- Picks new random number
    print("\nLet me guess... You are", number, "years old?")
    guess = input("'Higher', 'Lower', or was it 'Correct'? ")
    guess = guess.lower() #<- Lowercases
    tries += 1 #<- Ups the tries by one


print("\nPfft. Knew it all along.")
time.sleep(10)
