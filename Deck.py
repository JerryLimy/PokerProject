'''
Created on Apr 4, 2023

@author: limuyang
'''
import Card
import random
suits = ("diamonds","clubs", "spades", "hearts")
# Class model: Deck
# The attributes: deck which is a list of cards
# Major algorithms implemented: 
    #shuffle method: importing random to randomize all the card in the deck list. 
    #deal_card method: return none if deck list don't have any cards. If we have cards in deck the give a card out.
#List method and tuple requirements:pop,insert,clear,extend
class Deck: 
    def __init__(self):
        self.deck =[]
        suit_cards = []
        for s in suits: 
            suit_cards.clear()
            for x in range(2,15):
                suit_cards.insert(0,Card.Card(x,s))              
            self.deck.extend(suit_cards)    

    def get_deck(self):
        return self.deck
    
    def print_deck(self):
        [print(x) for x in self.deck]
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)
        
        