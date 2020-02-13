import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(0, 12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_suit(self):
        card = cards.Card(1,0)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_str(self):
        card = cards.Card(3,13)
        self.assertEqual(str(card), "King of Spades")

    def test_4_52(self):
        card = cards.Deck()
        self.assertEqual(len(card.cards), 52)

    def test_5_card(self):
        deck = cards.Deck()
        card = cards.Card()
        self.assertEqual(type(deck.deal_card()), type(card))

    def test_6_less(self):
        deck = cards.Deck()
        original_len = len(deck.cards) #52
        deck.deal_card()
        self.assertEqual(len(deck.cards), original_len-1)

    def test_7_replace(self):
        deck = cards.Deck()
        full_deck = len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        self.assertEqual(len(deck.cards), full_deck)

    def test_8_card(self):
        deck = cards.Deck()
        full_deck = len(deck.cards)
        card = deck.deal_card()
        deck.replace_card(card)
        deck.replace_card(card)
        self.assertEqual(len(deck.cards), full_deck)

############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
