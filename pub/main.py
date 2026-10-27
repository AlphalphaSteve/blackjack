import random

cards = [1,2,3,4,5,6,7,8,9,10,11]

def new_card():
    number = cards[random.randint(0, 10)]
    return number

player_total = 0
dealer_total = 0
dealer_total_pub = 0
player_stay = False
dealer_stay = False

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
        player_stay = False
        if player_total > 21:
            print(f"You busted with a total of {player_total} game over!")
            break
        else:
            print(f"You have a total of: {player_total}")
    else:
        print("Okay so you've decided to stay.")
        player_stay = True
    if dealer_total > 16:
        print("The dealer stands at a visible total of: " + str(dealer_total_pub))
        dealer_stay = True
        if player_stay == True and dealer_stay == True:
            finish = input("Would you like both you and the dealer to show their cards? ")
            if finish.lower() == "yes" or finish.lower() == "y":
                if player_total > dealer_total:
                    print("Great job you win with a total of: " + str(player_total) + ". And the dealer looses with a total of: " + str(dealer_total))
                    break
                if player_total < dealer_total:
                    print("Unfortunately the dealer won with a total of: " + str(dealer_total) + ". And you lost with a total of: " + str(player_total))
                    break
                else:
                    print("It's a tie looks like you need to go again!")
                    player_total = 0
                    dealer_total = 0
                    dealer_total_pub = 0
                    player_stay = False
                    dealer_stay = False
    elif dealer_total <= 16:
        card1 = new_card()
        dealer_stay = False
        dealer_total += card1
        dealer_total_pub += card1
        if dealer_total > 21:
            print("The dealer busted at a full total of: " + str(dealer_total))
            print("You win!")
            break
        else:
            print("The dealer hits to a new visible total of: " + str(dealer_total_pub))
