true_check = False
auction = {}
while not true_check:
    name = input("What is your name")
    bid = int(input("What is your bid: $"))
    auction[name] = bid
    bidder_check = input("Are there any other bidders? Type 'yes' or 'no'")
    if bidder_check != 'yes':
        true_check = True
print(f"The winner is {max(auction, key=auction.get)} with bid of ${max(auction.values())}")
