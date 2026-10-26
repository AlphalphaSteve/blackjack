import random
print("Hello gambling!")
cards = [1,2,3,4,5,6,7,8,9,10,11]

def new_card():
    number = cards[random.randint(0, 10)]
    return number
print(new_card())
