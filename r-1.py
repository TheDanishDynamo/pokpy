import random
suit_a_cards = ['A1','A2','A3','A4']
suit_b_cards = ['B1','B2','B3','B4']
deck_sorted = suit_a_cards + suit_b_cards
deck_shuffled = random.sample(deck_sorted, len(deck_sorted))

# draw a card
card_1 = random.choice(deck_shuffled)
deck_shuffled.remove(card_1)

# draw a second card
card_2 = random.choice(deck_shuffled)
deck_shuffled.remove(card_2)

print(deck_shuffled)
print(card_1,card_2)


