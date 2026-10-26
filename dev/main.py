import random
print("Hello gambling!")
cards = [1,2,3,4,5,6,7,8,9,10,11]

def new_card():
    number = cards[random.randint(0, 10)]
    return number


def dealer_card():
    number = cards[random.randint(0, 10)]
    return number
dealer_first_hand = dealer_card() + dealer_card()
player_first_hand = new_card() + new_card()
print("Your first hand total is: " + player_first_hand)
hit_or_stay = input("Would you like to hit or stay?")