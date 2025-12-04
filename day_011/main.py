import random
import art
def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user = []
    computer = []
    for x in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))
    user_score = sum(user)
    computer_score = sum(computer)
    input1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if input1 == "y" :
        print("" * 100)
        print(art.logo)
        def ace():
            if user_score > 21 :
                for a in range(len(user)) :
                    if user[a] == 11 :
                        user[a] = 1
                if user[0] == 1 :
                    user[0] = 11
        ace()
        def ace1 ():
            if computer_score > 21 :
                for a in range(len(user)):
                    if computer[a] == 11 :
                        computer[a] = 1
                computer[0] = 11
        ace1()
        print(f"Your cards : {user}, current score: {sum(user)}")
        computers_first_card = computer[0]
        print(f"Computer's first card {computers_first_card}")

        def reprt():
            print(f"Your final hand {user} , final score {user_score}")
            print(f"computer's final hand {computer} final score {computer_score}")
        def blackjack1() :
            if computer_score == 21:
                reprt()
                print("Black Jack.You Lose")
            elif user_score == 21 and computer_score != 21 :
                reprt()
                print("Blackjack. You win ")
            return
        blackjack1()
        to_continue = True
        while to_continue:
            user_input = input(f"Type 'y' to draw. Type 'n' to pass.").lower()
            if user_input == "y":
                user.append(random.choice(cards))
                ace()
                user_score = sum(user)
                if computer_score < 17:
                    sum_less = True
                    while sum_less:
                        computer.append((random.choice(cards)))
                        ace1()
                        computer_score = sum(computer)
                        if computer_score > 16:
                            sum_less = False
                            to_continue = False
                print(f"Your cards {user}, current score = {user_score}")
                if user_score > 21 :
                    if computer_score < 17:
                        sum_less = True
                        while sum_less:
                            computer.append((random.choice(cards)))
                            ace1()
                            computer_score = sum(computer)
                            if computer_score > 16:
                                sum_less = False
                                to_continue = False
                else :
                    to_continue = False
            elif user_input == "n" :
                if computer_score < 17 :
                    sum_less = True
                    while sum_less :
                        computer.append((random.choice(cards)))
                        ace1()
                        computer_score = sum(computer)
                        if computer_score > 16 :
                            sum_less = False
                            to_continue = False
                else :
                    to_continue = False
        def reprt():
            print(f"Your final hand {user} , final score {user_score}")
            print(f"computer's final hand {computer} final score {computer_score}")
        if computer_score > 21 :
            reprt()
            print("Computer went over. You win")
        elif 21 >= user_score > computer_score :
            reprt()
            print("You win")
        elif computer_score == user_score :
            reprt()
            print("Draw")
        else:
            reprt()
            print("You lose")
        blackjack()
blackjack()




