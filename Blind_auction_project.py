
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")


should_continue = True
bid = {}
while should_continue:
    name = input("What is your name? ")
    price = float(input("What is your bid amount? $"))
    bid[name] = price
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': ")
    print("\n" * 100)
    if continue_bidding == 'no':
        should_continue = False
        find_highest_bidder(bid)


