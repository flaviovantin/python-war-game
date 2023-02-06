import unittest
from card import Card
from deck import Deck
from player import Player


class TestWarGame(unittest.TestCase):

    def test_card_creation(self):
        two_hearts = Card('Hearts', 'Two')
        self.assertEqual('Two of Hearts (2)', str(two_hearts))
        four_diamonds = Card('Diamonds', 'Four')
        self.assertEqual('Four of Diamonds (4)', str(four_diamonds))
        jack_clubs = Card('Clubs', 'Jack')
        self.assertEqual('Jack of Clubs (11)', str(jack_clubs))
        ace_spades = Card('Spades', 'Ace')
        self.assertEqual('Ace of Spades (14)', str(ace_spades))
        
    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(52, len(deck))
        self.assertEqual('Two of Hearts (2)', str(deck.all_cards[0]))
        self.assertEqual('Three of Hearts (3)', str(deck.all_cards[1]))
        self.assertEqual('Ace of Clubs (14)', str(deck.all_cards[51]))
        
    def test_deck_shuffling(self):
        """
        This test may fail depending on the 'random.shuffle' result
        """
        deck = Deck()
        self.assertEqual('Two of Hearts (2)', str(deck.all_cards[0]))
        self.assertEqual('Ace of Clubs (14)', str(deck.all_cards[51]))
        deck.shuffle()
        self.assertNotEqual('Two of Hearts (2)', str(deck.all_cards[0]))
        self.assertNotEqual('Ace of Clubs (14)', str(deck.all_cards[51]))
        
    def test_deck_deal_one_card(self):
        deck = Deck()
        self.assertEqual(52, len(deck))
        card1 = deck.deal_one_card()
        self.assertEqual(51, len(deck))
        self.assertIsNotNone(card1)
        card2 = deck.deal_one_card()
        self.assertEqual(50, len(deck))
        self.assertIsNotNone(card2)
        self.assertEqual('King of Clubs (13)', str(card2))
        
    def test_player_creation(self):
        player_one = Player('Tobias')
        two_hearts = Card('Hearts', 'Two')
        four_diamonds = Card('Diamonds', 'Four')
        ace_spades = Card('Spades', 'Ace')
        cards = list((two_hearts, four_diamonds, ace_spades))
        player_one.add_multiple_cards(cards)
        self.assertEqual('Player Tobias has 3 cards in their hand', str(player_one))
        five_clubs = Card('Clubs', 'Five')
        player_one.add_card(five_clubs)
        self.assertEqual('Player Tobias has 4 cards in their hand', str(player_one))
        card = player_one.play_card()
        self.assertEqual('Two of Hearts (2)', str(card))
        self.assertEqual('Player Tobias has 3 cards in their hand', str(player_one))
        player_one.play_card()
        player_one.play_card()
        player_one.play_card()
        self.assertEqual('Player Tobias has 0 cards in their hand', str(player_one))
        another_card = player_one.play_card()
        self.assertIsNone(another_card)
        queen_hearts = Card('Hearts', 'Queen')
        player_one.add_multiple_cards(queen_hearts)
        self.assertEqual('Player Tobias has 0 cards in their hand', str(player_one))


if __name__ == '__main__':
    unittest.main()
