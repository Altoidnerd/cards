#!/usr/bin/env python3

import itertools, random
from pokerHands import *

# create deck
deck = getDeck()

num_players = int(input("Enter the number of players: "))
player_cards = []
player_names = []
player_hands = []

for i in range(1, num_players+1):
    player = str(input("Player %i name: " % i))
    exec("player_names.append('%s')" % player)
    exec("%s = OrderedCards()"  % player)
    exec("player_cards.append(%s)" % player)

burn = OrderedCards()
community = OrderedCards()

for player in player_cards:
    deck.deal(2, player)

for i in range(0, num_players):
    print("%s's hand: " % player_names[i], player_cards[i])

deck.deal(1,burn)
deck.deal(3,community)

print("Flop: " + str(community))

deck.deal(1,burn)
deck.deal(1,community)

print("Turn: " + str(community))

deck.deal(1,burn)
deck.deal(1,community)

print("River: " + str(community))

for i in range(1, num_players+1):
    name_ = player_names[i-1]
    cards_ = player_cards[i-1]
    exec("com%s = OrderedCards(community.cards_list[:])" % i)
    exec("com%s.deal(5,%s)" % (i, name_))
    exec("%sHand = evalHand(%s)" % (name_, name_))
    exec("print('%s has... ', str(%sHand))" % (name_,name_)) 
    exec("this_hand = %sHand" % name_)
    exec("player_hands.append(%sHand)" % name_)

def filterByMax(li):
    filtered = []
    for x in li:
        if x == max(li):
            filtered.append(li.index(x))
        else:
            pass
    return filtered

winner_index = filterByMax(player_hands)
if len(winner_index) > 1:
    print("Push!")
else:
    winner = player_names[winner_index[0]]
    print("%s wins! " % winner)
