from replit import clear

from art import logo

print (logo)

bids = {}
bidding_finished = False
  
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner}, with a bid value of ${highest_bid}.")

while not bidding_finished:   
  name = input("What is your  name: ")
  bid_value = int(input("What is your bid? $"))
  bids[name] = bid_value
  bidder_status = input("Are there any other bidders? type 'yes' or 'no'.")
  if bidder_status == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif bidder_status =="yes":
    clear()
