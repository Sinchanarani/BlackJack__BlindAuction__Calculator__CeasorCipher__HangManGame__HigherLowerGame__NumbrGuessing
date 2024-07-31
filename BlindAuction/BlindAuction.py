import Art

print(Art.logo)


#initialising empty dictionary
records={}
while True:
    name = input("What's your name?: ")
    bid = int(input("What is your bid? $"))
    competitors = input("Are there any other bidders? Type yes or no: ").lower()
    records[name] = bid
    if competitors == 'yes':
        continue
    else:
        break

winner=0
for key in records:
    winner_score=max(records.values())
for (key,values) in records.items():
    if values==winner_score:
        winner=key
print(f"The winner is {winner} with a bid of ${winner_score}")