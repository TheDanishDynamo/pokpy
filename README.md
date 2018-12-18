# pokpy
Poker w Python

Requirements 

## R-1 Calculate rankings
This a challenge that got me started, where I wanted to use python to find the rankings based on random draws of 5 cards, also called brute force guessing, the least frequent combination should be a royal flush, which is also the righest ranking in the official rankings of the game. The most frequent combination should be randome cards with no pairs. I want to persist and reuse previous results. Optionally divide an conquer to distribute processing and create more accurate result. I want to create a small example with reduced deck of, say two suits A and B and 4 cards, A1,B1,..,A4,B4 each with a draw of two cards, if the theory holds the least common combination with highest value shold be [A3,A4] and [B3,B4]. These approaches will be detailed in the technical section of the R-1 requirement. 

## R-2 Calculate strength of hand

**Subjectively**
This is the strength, as seen by one player. E.g. if the player is dealy two aces, he would have a very strong hand. If he has a 2 club and a 6 spade, it's considered a weak hand as the chances for winning are less than two aces. The 2 and 6 does not have any ranking other than the high card of 7 which only rank in the bottom 7 of of 14 cards. 

**Obectively**
The is the relative strength as seen of a spectator, e.g. in WSOP on TV. The viewer can se the cards of both players. When the initial cards are dealt (pre-flop), the strenght in % can be calculated by simple statistics or modeling.  Higher cards >7 and pairs, matching suit and close proximity are stronger than lower cards <=7 with mismatching suit and far proximity. 

These approaches will be detailed in the technical section of the R-2 requirement. 

## Poker Terminology
#The Deck
There are 52 cards in a deck, divided into four suits of 13 ranks each. 

#The Four Suits
There are 4 categories of cards called, Clubs, Hearts, Spades and Diamonds. 

#The 13 Ranks
In Poker, the Ace is the highest card and the 2 card (Deuce) is the lowest. However, the Ace can also be used as a low card, with the value of 1. The card values are:

1,2,3,4,5,6,7,8,9,10,11,12,13, and the alternate or common names for the same values are
(optionally Ace),2 or deuce,3,4,5,6,7,8,9,10,jack,queen,king,(optionally Ace)

1) Hand Strength
2) Royal Flush
3) Straight Flush
4) Four of a kind
5) Full House
6) Flush
7) Straight
8) Three of a kind
9) Two pairs
10) One pair
11) High Card

https://www.pokerstars.com/poker/terms/
http://www.wsop.com/poker-hands/

## R-1 Calculate rankings - Technical Specification

### POC - Tracer Bullet
Create a mini deck with 8 cards; two suits A and B, each with ranks 1,2,3,4. The 1 is called Ace and counts as a 1 or an Ace (virtually A5 or B5)
deck_sorted = ["A1","A2","A3","A4","B1","B2","B3","B4"]



