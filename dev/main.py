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

while True :
    if len(player_cards) == 0:
        player_cards.append(new_card())
        player_cards.append(new_card())
        print(f"You start with a {player_cards[0].card_name} and a {player_cards[1].card_name}, to a total of {get_total(player_cards)}")
    if len(dealer_cards) == 0:
        dealer_cards.append(new_card())
        dealer_total_pub = get_total(dealer_cards);
        dealer_cards.append(new_card())
        print(f"The dealer has a face up total of: {dealer_total_pub}")
    hit = input("Would you like to hit or stay? ")
    if hit.lower() == "hit" :
        player_cards.append(new_card())
        player_total = get_total(player_cards)
        if player_total > 21:
            print(f"You busted with a total of {player_total} game over!")
            break
        else:
            print(f"You have a total of: {player_total}")
    else:
        print("Okay so you've decided to stay.")
        break
    if get_total(dealer_cards) > 16:
        print("The dealer stands at a visible total of: " + str(dealer_total_pub))
    elif get_total(dealer_cards) <= 16:
        dealer_card = new_card()
        dealer_cards.append(new_card())
        dealer_total_pub += dealer_card.card_value
        if get_total(dealer_cards) > 21:
            print(f"The dealer busted at a full total of: {get_total(dealer_cards)}")
            print("You win!")
            break
        else:
            print(f"The dealer hits to a new visible total of: {dealer_total_pub}")
