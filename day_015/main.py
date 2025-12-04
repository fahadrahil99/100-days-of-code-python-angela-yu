
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Money = {"a":0}

def coffee_machine():
    to_continue = True
    while to_continue:
        c_input = input("What would you like? (espresso/latte/cappuccino):").lower()


        def fund (q,d,n,p):
            return 0.25*q + 0.1 * d + 0.05 * n + 0.01* p

        def coffee(c_type):
            water = MENU[c_type]["ingredients"]["water"]
            milk = MENU[c_type]["ingredients"]["milk"]
            c_coffee = MENU[c_type]["ingredients"]["coffee"]
            if resources["water"] - water >= 0:
                resources["water"] -= water
                if resources["milk"] - milk >= 0:
                    resources["milk"] -= milk
                    if resources["coffee"]- c_coffee >= 0:
                        resources["coffee"]-= c_coffee
                        print("Please insert coin.")
                    else:
                        print("Sorry there is not enough coffee beans.")
                        coffee_machine()
                else:
                    print("Sorry there is not enough milk.")
                    coffee_machine()
            else:
                print("Sorry there is not enough water.")
                coffee_machine()

        # # def report(c_resources,money):
        #         print(f"Water : {c_resources[0]}")
        #         print(f"Milk :{c_resources[1]}")
        #         print(f"Coffee : {c_resources[2]}")
        #         print(f"Money : {money}")


        if c_input == "espresso" or c_input == "latte" or c_input == "cappuccino":
            quarter = int(input("How many quarters?:"))
            dimes = int(input("How many dimes?:"))
            nickel = int(input("How many nickels?:"))
            penny = int(input("How many pennies?:"))
            funds = fund(quarter,dimes,nickel,penny)
            if funds - MENU[c_input]["cost"] >= 0 :
                coffee(c_input)
                Money["a"] += MENU[c_input]["cost"]
                print(f"Here is your {c_input} .Enjoy!")
                print(f"Here is ${round(funds-MENU[c_input]["cost"],2)} change.")
            else:
                print("Sorry that's not enough money. Money refunded.")




        elif c_input == "report":
            print(f"Water : {resources["water"]}")
            print(f"Milk :{resources["milk"]}")
            print(f"Coffee : {resources["coffee"]}")
            print(f"Money : ${Money["a"]}")
        else:
            to_continue = False
coffee_machine()