from card import Card
import random


class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card(suit, rank)
                self.all_cards.append(card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one_card(self):
        return self.all_cards.pop()
                
    def __len__(self):
        return len(self.all_cards)
        
    def __str__(self):
        descr = ''
        for card in self.all_cards:
            descr += str(card) + '\n'
        return descr

