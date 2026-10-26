import random
print("Hello gambling!")
cards = [1,2,3,4,5,6,7,8,9,10,11]

def new_card():
    number = cards[random.randint(0, 10)]
    return number

player_total = 0
dealer_total = 0
dealer_total_pub = 0

while True :
    if player_total == 0:
        player_total += new_card()
        player_total += new_card()
        print("Your starting total is: " + str(player_total))
    if dealer_total == 0:
        card1 = new_card()
        dealer_total += card1
        dealer_total_pub += card1
        dealer_total += new_card()
        print("The dealer has a face up total of: " + str(dealer_total_pub))
    break
print(new_card())
