from sys import modules

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors.\n"))
if a == 0 :
    print(rock)
elif a==1 :
    print(paper)
elif a== 2 :
    print(scissors)
else :
    print("You typed wrong input")

import random

hands = [rock,paper,scissors]
b = random.randint(0,2)
if a == 1 or a ==2 or a== 0 :
    print("Computer Chose: \n",hands[b])
else :
    print("You Lose")

if a == b :
    print("it's a draw")
elif a == 0 and b == 1 or a== 1 and b== 2 or a==2 and b==0 :
    print (" You Lose")

elif  a == 1 and b == 0 or  a== 2 and b== 1  or a==0 and b==2 :
    print ("You Win")










