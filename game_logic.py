from player import Player
from deck import Deck


# Game setup
player_one = Player('One')
player_two = Player('Two')

deck = Deck()
deck.shuffle()
while len(deck) > 0:
    player_one.add_card(deck.deal_one_card())
    player_two.add_card(deck.deal_one_card())

WAR_CARDS = 5
game_round = 0
game_on = True
while game_on:
    game_round += 1
    print(f'Round {game_round} Fight!')
    
    if len(player_one.cards) == 0:
        print(f'Player {player_one.name} has zero cards! Player {player_two.name} wins!')
        game_on = False
        continue
    if len(player_two.cards) == 0:
        print(f'Player {player_two.name} has zero cards! Player {player_one.name} wins!')
        game_on = False
        continue

    # Start of the round
    player_one_table_cards = []
    player_one_table_cards.append(player_one.play_card())
    
    player_two_table_cards = []
    player_two_table_cards.append(player_two.play_card())
    
    at_war = True
    while at_war:
        if player_one_table_cards[-1].value > player_two_table_cards[-1].value:
            player_one.add_multiple_cards(player_one_table_cards)
            player_one.add_multiple_cards(player_two_table_cards)
            at_war = False

        elif player_one_table_cards[-1].value < player_two_table_cards[-1].value:
            player_two.add_multiple_cards(player_two_table_cards)
            player_two.add_multiple_cards(player_one_table_cards)
            at_war = False

        else:
            print('WAR!')
            if len(player_one.cards) < WAR_CARDS:
                print(f"Player {player_one.name} doesn't have enough cards! Player {player_two.name} wins!")
                game_on = False
                break
            if len(player_two.cards) < WAR_CARDS:
                print(f"Player {player_two.name} doesn't have enough cards! Player {player_one.name} wins!")
                game_on = False
                break
            for _ in range(WAR_CARDS):
                player_one_table_cards.append(player_one.play_card())
                player_two_table_cards.append(player_two.play_card())
