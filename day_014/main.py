import random

import art
import game_data
print(art.logo)

compare_a = random.choice(game_data.data)
against_b = random.choice(game_data.data)
def same(a,b):
    while a == b:
     return  random.choice(game_data.data)

def comparison (compare,against):
    if compare['follower_count'] > against['follower_count']:
        return compare['follower_count']
    else:
        return against['follower_count']
def a_b(choice):

    if choice == "a":
        return compare_a['follower_count']
    elif choice == "b" :
        return against_b['follower_count']
score = 0
game_over = False
while not game_over:
    while against_b == compare_a:
        against_b = same(compare_a,against_b)
    print(f"Compare A : {compare_a['name']}, a {compare_a['description']},from {compare_a['country']}")
    print(art.vs)
    print(f"Against B : {against_b['name']}, a {against_b['description']},from {against_b['country']}")
    Input = input("Who has more followers? A or B.").lower()
    if a_b(Input) >= comparison(compare_a,against_b) :
        score += 1
        compare_a = against_b
        against_b = random.choice(game_data.data)
        print("\n"*20)
        print(art.logo)
        print(f"You are right! Current score {score}")

    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry, That's wrong. Final score {score}")
        game_over = True
