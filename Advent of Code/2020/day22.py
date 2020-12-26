# Day 22: Crab Combat
# Part 1: 34127
# Part 2: 32054

from pathlib import Path
from collections import deque

INPUT = Path('input_22.txt')
DEBUG = False


class Deck:
    def __init__(self, cards: [int]):
        self._cards = deque(cards)


    def deck(self) -> [int]:
        '''Returns the cards in the deck'''
        return self._cards

    
    def deck_size(self) -> int:
        '''Returns the number of cards in the deck'''
        return len(self._cards)

        
    def get_top_card(self) -> int:
        '''Returns the value of the top card and removes it from the deck'''
        return self._cards.popleft()


    def add_cards_to_bottom(self, card_1: int, card_2: int) -> None:
        '''Adds a given card to the bottom of the deck'''
        self._cards.append(card_1)
        self._cards.append(card_2)


    def get_score(self) -> int:
        '''Returns the player's score'''
        score = 0
        for index in range(self.deck_size()):
            score += self._cards[index] * (self.deck_size() - index)
        return score

        
def run() -> None:
    print(get_first_ans())
    print(get_second_ans())
    


def get_first_ans() -> int:
    '''Plays a game of Combat and returns the winning player's score'''
    player_1, player_2 = _get_decks()
    winner = _combat(player_1, player_2)[0]
    return winner.get_score()



def get_second_ans() -> int:
    '''Plays a game of Recursive Combat and returns the winning player's score'''
    player_1, player_2 = _get_decks()
    winner = _combat(player_1, player_2, recursive = True)[0]
    return winner.get_score()


def _combat(deck_1: Deck, deck_2: Deck, recursive = False) -> (Deck, int):
    '''Plays a game of Combat and returns the winning deck'''
    player_1 = Deck(deck_1.deck())
    player_2 = Deck(deck_2.deck())
    total_cards = player_1.deck_size() + player_2.deck_size()
    known_arrangements = []

    if DEBUG:
        print(player_1.deck())
        print(player_2.deck())
        print()

    while player_1.deck_size() < total_cards and \
          player_2.deck_size() < total_cards:

        if recursive:
            _deck_1 = list(player_1.deck())
            _deck_2 = list(player_2.deck())
            
            if _deck_1 in known_arrangements and \
               _deck_2 in known_arrangements:
                return player_1, 1
            else:
                if not _deck_1 in known_arrangements:
                    known_arrangements.append(_deck_1)
                if not _deck_2 in known_arrangements:
                    known_arrangements.append(_deck_2)
            
        card_1 = player_1.get_top_card()
        card_2 = player_2.get_top_card()

        if recursive and \
           len(player_1.deck()) >= card_1 and \
           len(player_2.deck()) >= card_2:
            player_num = _combat(
                Deck(list(player_1.deck())[:card_1]),
                Deck(list(player_2.deck())[:card_2]), recursive)[1]
                
            if player_num == 1:
                player_1.add_cards_to_bottom(card_1, card_2)
            else:
                player_2.add_cards_to_bottom(card_2, card_1)                
        else:
            if card_1 > card_2:
                player_1.add_cards_to_bottom(card_1, card_2)
            else:
                player_2.add_cards_to_bottom(card_2, card_1)

        if DEBUG:
            print(player_1.deck())
            print(player_2.deck())
            print()
    
    if player_1.deck_size() > player_2.deck_size():
        return player_1, 1
    else:
        return player_2, 2



def _get_decks() -> (Deck):
    '''
    Finds the text file specified by INPUT and returns its content as a tuple
    containing the decks of both players.
    '''
    file = open(INPUT, 'r')
    deck_1 = []
    deck_2 = []
    player = 0

    for line in file:
        if line[:-1] == 'Player 1:':
            player = 1
        elif line[:-1] == 'Player 2:':
            player = 2
        elif line[:-1] != '':
            if player == 1:
                deck_1.append(int(line[:-1]))
            elif player == 2:
                deck_2.append(int(line[:-1]))
    
    file.close()
    return Deck(deck_1), Deck(deck_2)
    
if __name__ == '__main__':
    run()
