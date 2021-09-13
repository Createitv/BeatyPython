# -*- coding: utf-8 -*-
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck():
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamands clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = FrenchDeck()
print(deck[0])
from random import choice
print(choice(deck))