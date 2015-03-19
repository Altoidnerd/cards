#/usr/bin/env python3

import itertools
import random
from pokerHands import *

class Table(object):
    def __init__(self, players=None, pot=None):
        if players is None:
            self.players = None
        else:
            self.players = players 
        if pot is None:
            self.pot = 0
        else: self.pot = pot
    def setLimit(self, lim):
        self.limit = lim
    def __str__(self):
        return str(self.players) +"  Table Pot:" + str(self.pot)
    def __repr__(self):
        return self.__str__()


class Player(object):
    def __init__(self, name, credit=None, cards=None):
        self.name = name
        if credit is None:
            self.balance = 0
        else:
            self.balance = credit
        if cards is None:
            self.cards = OrderedCards()
            self.cards_list = []
        else:
            self.cards = OrderedCards(cards)
            self.cards_list = cards.cards_list()
        self.action=False

    def __str__(self):
        return "name: "+self.name+", balance: "+str(self.balance)+", cards: "+str(self.cards_list)
    def __repr__(self):
        return self.__str__()
    def bet(self, amount, pot):
        if self.balance - amount < 0:
            raise ValueError("Bet exceeds balance!")
        else:            
            self.balance -= amount
            pot.balance += amount
            print("The pot is now %s" % pot.balance)
            return pot.balance

    def credit(self, amount):
        self.balance += amount
        return self

    def debit(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Debit exceeds balance!")
        else:
            self.balance -= amount
            return self

a=Player('al', 1000)
b=Player('fred', 1000)
c=Player('sheryl', 1000)
t=Table(players=[a,b,c], pot=0)

