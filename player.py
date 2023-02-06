class Player():

    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def play_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print('There are no cards to play. Probably, you lost the game :(')
            return None
        
    def add_card(self, card):
        self.cards.append(card)
        
    def add_multiple_cards(self, cards):
        if type(cards) == list:
            self.cards.extend(cards)
        else:
            print("It's not a list of Cards, sorry!")

    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards in their hand'

