import random
import sys

def guessnum():
  random_num = random.randint(1,6)
  awnser = int(input ("what do you think the number is? "))
  if awnser==random_num:
    print("good job. you are correct. ")
  else:
    print("incorrect. better luck next time. ")

restart = input("would you like to try again? ")
if restart.title() in ["Yes" or "y"]:
  guessnum()
else:
  end()

  def end():
    print('Goodbye!')
    sys.exit(0)

    guessnum()
