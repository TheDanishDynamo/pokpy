import random

hearts = ["H"+str(card) for card in range(14)]
diamonds = ["D"+str(card) for card in range(14)]
clubs = ["C"+str(card) for card in range(14)]
spades = ["S"+str(card) for card in range(14)]
deck_sorted = hearts + diamonds + clubs + spades
print(deck_sorted)
deck_randomized = random.sample(deck_sorted, len(deck_sorted))
print(deck_randomized)
print(len(deck_randomized))
players = 2
hands = [[None,None],[None,None]]
hands[0][0] = random.choice(deck_randomized)
deck_randomized.remove(hands[0][0])
print(hands[0][0])
print(len(deck_randomized))
hands[1][0] = random.choice(deck_randomized)
deck_randomized.remove(hands[1][0])
print(hands[1][0])
print(len(deck_randomized))
hands[0][1] = random.choice(deck_randomized)
deck_randomized.remove(hands[0][1])
print(hands[0][1])
print(len(deck_randomized))
hands[1][1] = random.choice(deck_randomized)
deck_randomized.remove(hands[1][1])
print(hands[1][1])
print(len(deck_randomized))
print(hands)
flop = [random.choice(deck_randomized),random.choice(deck_randomized),random.choice(deck_randomized)]
print(flop)
deck_randomized.remove(flop[0])
deck_randomized.remove(flop[1])
deck_randomized.remove(flop[2])
print(len(deck_randomized))



