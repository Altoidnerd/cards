#/usr/bin/env python3

import itertools
import random
from pokerHands import *

class BankRoll(object):
    def __init__(self, balance=None):
        if (balance is None):
            balance = 0
        self.balance = balance

    def __str__(self):
        return str(self.balance)

    def __repr__(self):
        return str(self.balance)

    def bet(self, amount, pot):
        if self.balance - amount < 0:
            raise ValueError("bet exceeds balance!")
        else:
            self.balance -= amount
            pot.balance += amount
            print("The pot is now %s" % pot.balance)
            return pot.balance

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        self.balance -= amount
        return self.balance
##test helper pot
pot = BankRoll()
##


class Table(object):
    def __init__(self, players):
        self.players = players 
    def action(self): 
        for k in players:
            if k.action == True:
                return k
            else:
                pass
       
class Player(object):
    def __init__(self, name, credit=None, cards=None):
        self.name = name
        if credit is None:
            self.bankroll = BankRoll()
        else:
            self.bankroll = BankRoll(credit)
        if cards is None:
            self.cards = OrderedCards()
        else:
            self.cards = OrderedCards(cards)
        self.action = False
    
    def __str__(self):
        return self.name+": "+str(self.bankroll)+"; "+str(self.cards)
    def __repr__(self):
        return self.__str__()

