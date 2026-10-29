import random

from cards import Cards


def new_card():
    return random.choice(list(Cards))

def get_total(card_list):
    total = 0
    for card in card_list:
        total += card.card_value
    return total

player_cards = []
dealer_cards = []
dealer_total_pub = 0
player_stay = False
dealer_stay = False

while True :
    if get_total(player_cards) == 0:
        player_cards.append(new_card())
        player_cards.append(new_card())
        print(f"Your starting total is: {get_total(player_cards)}")
    if get_total(dealer_cards) == 0:
        card1 = new_card()
        dealer_cards.append(card1)
        dealer_total_pub += card1.card_value
        dealer_cards.append(new_card())
        print(f"The dealer has a face up total of: {dealer_total_pub}")
    hit = input("Would you like to hit or stay? ")
    if hit.lower() == "hit" :
        player_cards.append(new_card())
        player_stay = False
        if get_total(player_cards) > 21:
            print(f"You busted with a total of {get_total(player_cards)} game over!")
            break
        else:
            print(f"You have a total of: {get_total(player_cards)}")
    else:
        print("Okay so you've decided to stay.")
        player_stay = True
    if get_total(dealer_cards) > 16:
        print("The dealer stands at a visible total of: " + str(dealer_total_pub))
        dealer_stay = True
        if player_stay == True and dealer_stay == True:
            finish = input("Would you like both you and the dealer to show their cards? ")
            if finish.lower() == "yes" or finish.lower() == "y":
                if get_total(player_cards) > get_total(dealer_cards):
                    print("Great job you win with a total of: " + str(get_total(player_cards)) + ". And the dealer looses with a total of: " + str(get_total(dealer_cards)))
                    break
                if get_total(player_cards) < get_total(dealer_cards):
                    print("Unfortunately the dealer won with a total of: " + str(get_total(dealer_cards)) + ". And you lost with a total of: " + str(get_total(player_cards)))
                    break
                else:
                    print("It's a tie looks like you need to go again! " + str(get_total(player_cards)) + " " + str(get_total(dealer_cards)))
                    player_cards = []
                    dealer_cards = []
                    dealer_total_pub = 0
                    player_stay = False
                    dealer_stay = False
    elif get_total(dealer_cards) <= 16:
        card1 = new_card()
        dealer_stay = False
        dealer_cards.append(card1)
        dealer_total_pub += card1.card_value
        if get_total(dealer_cards) > 21:
            print("The dealer busted at a full total of: " + str(get_total(dealer_cards)))
            print("You win!")
            break
        else:
            print("The dealer hits to a new visible total of: " + str(dealer_total_pub))
