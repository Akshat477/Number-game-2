import random

list1 = [1,2,3,4,5,6,7,8,9]
number = random.choice(list1)

chances = 5 
while chances>0:
  guess = input("ENTER YOUR GUESS FROM 1-9")

  if guess == number : 
    print("CONGRATULATION YOU HAVE WON")

  if guess > number: 
      print("U WERE CLOSE, think about a lower number")

  if guess < number: 
      print("U WERE CLOSE, think about a greater number")

  chances-=1 
   

if chances == 0 :
    print("U LOOSE THE NUMBER WAS",number)