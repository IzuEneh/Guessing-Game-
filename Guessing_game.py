from random import *
rand_num = randint(1,101)

guess = [0]

while True:
    new_guess = int(input("hey guess a mnumber in between 1-100!"))
    guess.append(new_guess)
    
    if guess[-1] > 100 or guess[-1] < 1:
      print("OUT OF BOUNDS!)
    
    if guess[-1] == rand_num:
        print("CONGRATS YOU GOT IT !!")
        break
    elif abs(guess[-1]-rand_num)<= 10 and len(guess)==2:
        print("WARM")
    elif abs(guess[-1]-rand_num)>10 and len(guess)==2:
        print("COLD")
    elif abs(guess[-1]-rand_num)<abs(guess[-2]-rand_num):
        print("WARMER")
    elif abs(guess[-1]-rand_num)>abs(guess[-2]-rand_num):
        print("COLDER")
    
