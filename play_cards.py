from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Nellie")
d2 = CardDeck("Andy")
#  d1 = CardDeck.__init__(x)

print(type(d1))
print(type(d2))

print(d1.dealer_name)

d1.dealer_name = "Rosie"

print(d1.dealer_name)
print(d1.get_dealer_name())




for name in 'Bob', 'Martha', 123:
    try:
        d1.dealer_name = name
    except TypeError as err:
        print(err)
    else:
        print(d1.dealer_name.upper())

d1.shuffle()
print(d1.cards)
print()
for i in range(5):
    print(d1.draw())

print(d1.get_suits())  # CardDeck.get_suits(CardDeck)
print(CardDeck.get_suits())  # CardDeck.get_suits(CardDeck)
print('-' * 60)

j1 = JokerDeck('Frodo')
j1.shuffle()
print(j1.dealer_name)
print(j1.cards)

for i in range(10):
    print(j1.draw())
print()
