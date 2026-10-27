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
        player_total += new_card() + new_card()
        print(f"Your starting total is: {player_total}")
    if dealer_total == 0:
        card1 = new_card()
        dealer_total += card1
        dealer_total_pub += card1
        dealer_total += new_card()
        print(f"The dealer has a face up total of: {dealer_total_pub}")
    hit = input("Would you like to hit or stay? ")
    if hit.lower() == "hit" :
        player_total += new_card()
        if player_total > 21:
            print(f"You busted with a total of {player_total} game over!")
            break
        else:
            print(f"You have a total of: {player_total}")
    else:
        print("Okay so you've decided to stay.")
        break
    if dealer_total > 16:
        print("The dealer stands at a visible total of: " + str(dealer_total_pub))
    elif dealer_total <= 16:
        card1 = new_card()
        dealer_total += card1
        dealer_total_pub += card1
        if dealer_total > 21:
            print("The dealer busted at a full total of: " + str(dealer_total))
            print("You win!")
            break
        else:
            print("The dealer hits to a new visible total of: " + str(dealer_total_pub))
