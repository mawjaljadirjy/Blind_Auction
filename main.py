from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program. ")
auction_bidders={}
def blind_auction(name,bid):
  auction_bidders[name]=bid
  return(auction_bidders)
play="yes"  
while play=="yes":
  name=input("What is your name?: ").lower()
  bid=int(input("What's your bid?: $"))
  play= input("Are there any other bidders? Type 'yes' or 'no'").lower()
  if play=="yes":
    clear()
    blind_auction(name,bid)
    
else: 
  dict_auction=blind_auction(name,bid)
  highest_bidder=0
  winner=""
  for bidder in dict_auction:
    value=dict_auction[bidder]
    if value>highest_bidder:
      highest_bidder=value
      winner=bidder
  print(f"The winner is {winner} with a bid of {highest_bidder}$")
      
      
    
  


  


