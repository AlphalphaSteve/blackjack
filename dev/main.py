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

def dealer_card():
    number = cards[random.randint(0, 10)]
    return number
dealer_first_hand = dealer_card() + dealer_card()
player_first_hand = new_card() + new_card()
print("Your first hand total is: " + str(player_first_hand))
hit_or_stay = input("Would you like to hit or stay?")
