from art import logo

print(f"{logo} \n Welcome to the secret auction program")


def find_top_bidder(bidder_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidder_dict:
          bid_amount = bidder_dict[bidder]
          if int(bid_amount) > int(highest_bid):
               highest_bid=bid_amount
               winner = bidder
    print(f"The winner is {winner} with a bid {highest_bid}")


next_bidder = 'yes'
dict_bidders = {}
while next_bidder == 'yes':
    name = input("What is your name?")

    bid_val = input("What is your bid?")

    dict_bidders[name] = bid_val

    next_bidder = input("Are there any other bidders? 'yes' 'no'").lower()
    print("\n" * 100)

    if next_bidder == "no":
         find_top_bidder(dict_bidders)

# Source - https://stackoverflow.com/a/280156
# Posted by A. Coady
# Retrieved 2026-09-20, License - CC BY-SA 2.5

print(max(dict_bidders, key=dict_bidders.get)) #klucz z największą wartością

#max(dict_bidders.iterkeys(), key=(lambda key: dict_bidders[key]))


print(dict_bidders)





def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]

#print(keywithmaxval(dict_bidders))


