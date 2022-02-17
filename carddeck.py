import random

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # .toString()
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

# c = Card('10', 'Diamonds')
# print(c)     10-Diamonds
# print(repr(c))   Card('10', 'Diamonds')


class CardDeck:  # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer_name):
        self._dealer_name = dealer_name
        self._make_deck()


    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        random.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards

    # getter method
    def get_dealer_name(self):
        return self._dealer_name

    # (getter) property
    @property  # decorator
    def dealer_name(self):
        return self._dealer_name

    # dealer_name = property(dealer_name)

    # (setter) property
    @dealer_name.setter
    def dealer_name(self, name):
        if isinstance(name, str):
            self._dealer_name = name
        else:
            raise TypeError("dealer name must be a str")

    @classmethod
    def get_suits(cls):
        return cls.SUITS



