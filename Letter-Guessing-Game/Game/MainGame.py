import random 
import string 
global lives
lives = 2
global a
a = input("Enter a Letter:")
answer = ""
test = True
global random_letter
random_letter = random.choice(string.ascii_lowercase)
winMessage ="You Win!"
def reset():
  answer = input("Play again? Y/N")
  test = True
  while(test):
            if answer == "y" or answer =="Y":
                global lives
                lives = 2
                global random_letter
                random_letter = random.choice(string.ascii_lowercase)
                global a
                a = input("Enter a letter:")
                test = False
                    
            elif answer =="N" or  answer =="n":
                print ("Bye!")
                break
            else:
                answer = input("Invalid Response. Please try again. Play Again? Y/N")

while(lives > 0):
    if a == random_letter:
        print (winMessage)
        reset()            
    else:
        print( "You have",lives," lives left.")
        lives = lives -1
        a = input("Try again.")
    
    if lives == 0:
        print ("The letter was:"+ random_letter)
        reset()
