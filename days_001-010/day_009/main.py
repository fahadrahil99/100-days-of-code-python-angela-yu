import art
auction_data = {}
whether_to_continue = True
while whether_to_continue :
# TODO-1: Ask the user for input
    print(art.logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?:$ "))
    other_bidders = input("Are there any other bidders? Type 'Yes' or 'no'. \n").lower()
# TODO-2: Save data into dictionary {name: price}
    auction_data[name]=bid

# TODO-3: Whether if new bids need to be added
    if other_bidders == "yes" :
        print("\n"*100)
    else:
        whether_to_continue = False


# TODO-4: Compare bids in dictionary
winner = 0
winner1 = ""
for key in auction_data :
    if auction_data[key] > winner :
        winner = auction_data[key]
        winner1 = key

print(f"The winner is {winner1} with a bid of $ {winner}. ")


