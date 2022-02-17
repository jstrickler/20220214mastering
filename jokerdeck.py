
from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for joker_num in '1', '2':
            c = Card(joker_num, '*JOKER*')
            self._cards.append(c)
