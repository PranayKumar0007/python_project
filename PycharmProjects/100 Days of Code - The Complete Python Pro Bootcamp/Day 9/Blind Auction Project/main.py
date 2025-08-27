# TODO-1: Ask the user for input
name = input("What is your name? ")
price = float(input("What is your price? $"))
# TODO-2: Save data into dictionary {name: price}
bid={}
bid["name"]=price
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
print("Welcome to the Blind Auction!!")

def highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner =""
    for bidder in bidding_dictionary:
        bid_price = bidding_dictionary[bidder]
        if bid_price > highest_bid:
            highest_bid = bid_price
            winner = bidder
    print(f"""The winner is {winner} with a bid of ${highest_bid}""")

should_continue = True
while should_continue :
    name = input("What is your name? ")
    price = float(input("What is your price? $"))
    bid["name"] = price
    continue_not = input("Are there any other bidders? type 'yes' or 'no' ")
    if continue_not == 'no':
        should_continue = False
        highest_bidder()
    elif continue_not == 'yes':
        should_continue = True




