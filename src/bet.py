#/usr/bin/env python3

import itertools
import random
from pokerHands import *

class BankRoll(object):
    def __init__(self,balance=None):
        if(balance is None):
            balance = 0
        self.balance = balance

    def __repr__(self):
        return str(self.balance)

    def bet(self, amount, pot):
        self.balance -= amount
        pot.balance += amount
        return pot.balance

#    def call(self):
#        self.

    def credit(self, amount):
        self.balance += amount
        return self.balance

    def debit(self, amount):
        self.balance -= amount
        return self.balance

pot = BankRoll()


