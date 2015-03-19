#!/usr/bin/env python3

import itertools, random
from player import *

# create deck
deck = getDeck()

num_players = int(input("Enter the number of players: "))
players = []

for i in range(num_players):
    new = str(input("Player %i's name: " % i))
    players.append(Player(new, 1000))

t = Table(players, pot=0)

burn = OrderedCards()
community = OrderedCards()

for k in range(len(t.players)):
    deck.deal(2, t.players[k])

for i in range(0, num_players):
    print(players[i])

deck.deal(1,burn)
deck.deal(3,community)

print("Flop: " + str(community))

deck.deal(1,burn)
deck.deal(1,community)

print("Turn: " + str(community))

deck.deal(1,burn)
deck.deal(1,community)

print("River: " + str(community))

playerHands = []

for k in range(len(t.players)):
    com = OrderedCards(community.cards_list[:])
    com.deal(5,t.players[k])
    playerHands.append(evalHand(t.players[k].cards_list))


