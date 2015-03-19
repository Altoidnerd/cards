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

pot = BankRoll()


