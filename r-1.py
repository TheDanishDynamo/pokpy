import random
suit_h_cards = ['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13']
suit_c_cards = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13']
suit_s_cards = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13']
suit_d_cards = ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13']
deck_sorted = suit_h_cards + suit_c_cards + suit_s_cards + suit_d_cards

deck_shuffled = ['C8', 'H2', 'D12', 'S8', 'D4', 'D9', 'D6', 'S3', 'D10', 'C6', 'C3', 
'S7', 'C2', 'H6', 'D13', 'H8', 'D2','C12', 'D5', 'C13', 'C4', 'S10', 'C10', 'C5', 'H10', 
'H9', 'C11', 'S12', 'S13', 'H7', 'S9', 'D1', 'H4', 'H13', 'H11', 'H5', 'S6', 'C1', 'S11', 
'S1', 'S2', 'D8', 'S5', 'D11', 'D3', 'C9', 'H3', 'C7', 'H1', 'S4', 'H12', 'D7']
#deck_shuffled = random.sample(deck_sorted, len(deck_sorted))

print(deck_shuffled)

# draw the first card - player 1
player_1_card_1 = 'D8' 
player_1_card_1 = random.choice(deck_shuffled)
deck_shuffled.remove(player_1_card_1)

# draw the first card - player 2
player_2_card_1 = 'H1' 
player_2_card_1 = random.choice(deck_shuffled)
deck_shuffled.remove(player_2_card_1)

# draw the second card - player 1
player_1_card_2 = 'C9'
player_1_card_2 = random.choice(deck_shuffled)
deck_shuffled.remove(player_1_card_2)

# draw the second card - player 2
player_2_card_2 = 'C11' 
player_2_card_2 = random.choice(deck_shuffled)
deck_shuffled.remove(player_2_card_2)

print("player 1",[player_1_card_1,player_1_card_2])
print("player 2",[player_2_card_1,player_2_card_2])


print("deck",deck_shuffled)

# draw the first card - flop
flop_card_1 = 'S13' # 
#flop_card_1 = random.choice(deck_shuffled)
deck_shuffled.remove(flop_card_1)

# draw the second card - flop
flop_card_2 = 'H5' # 
#flop_card_2 = random.choice(deck_shuffled)
deck_shuffled.remove(flop_card_2)

# draw the third card - flop
flop_card_3 = 'H7' # 
flop_card_3 = random.choice(deck_shuffled)
deck_shuffled.remove(flop_card_3)

print("flop",[flop_card_1,flop_card_2,flop_card_3])
# ['S13', 'H5', 'C2']
print("deck",deck_shuffled)
p1hand = [player_1_card_1,player_1_card_2,flop_card_1,flop_card_2,flop_card_3]
p1hand.sort()
print("player 1 (sorted by suit-rank)",p1hand) 
# ['C13', 'C2', 'H5', 'H6', 'S13']
print("player 1 (sorted by rank)",['C2','H5', 'H6', 'C13', 'S13']) 
print("player 1 strength - individual","Manual strength")
p2hand = [player_2_card_1,player_2_card_2,flop_card_1,flop_card_2,flop_card_3]
p2hand.sort()
print("player 2 (sorted by suit-rank)",p2hand)
# ['C2', 'D5', 'H5', 'H9', 'S13']
print("player 2 (sorted by rank)",['C2', 'D5', 'H5', 'H9', 'S13']) 
print("player 2 strength - individual","Manual strength")
print("commentary#1: player 1 has two kings very good w 2 players")
print("commentary#2: player 2 has one pair, which is ok in a 2 player game, it could be a sneaker")

