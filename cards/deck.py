from random import *
from cards import card
class FiftyTwo:

    def generate_deck():
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        values = range(1, 14)

        placeholder_deck = []
        for i in suits:
            for j in values:
                placeholder_deck.append([i, j])

        deck_dealt = []
        for i in range(0, 52):
            new_card = card.Card()
            deck_dealt.append(new_card)

        for i in range(0, 52):
            card_pick = randint(0, len(placeholder_deck) - 1)
            pick_a_card = placeholder_deck[card_pick]
            placeholder_deck.pop(card_pick)
            deck_dealt[i].suit = pick_a_card[0]
            deck_dealt[i].value = pick_a_card[1]

        return deck_dealt

