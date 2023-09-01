'''
Created on Apr 4, 2023

@author: limuyang
'''
import Card
import Deck
import Display
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

rankNames = ("High Card","One Pair","Two Pair","Three-of-a-kind","Straight","Flush","Full House","Four-of-a-kind","Straight Flush","Royal Flush")  

#Class model:Hand
# The attributes: hand which is a list of dealt cards
# Major algorithms implemented: 
    #add_card method: using sorting method to put the cards in order from big value to small, 
#while add a card at end of the hand list. 
    ##rank method:The values of five cards of hand and lists of suits are 
    #extracted respectively, and the number of repeated occurrences of each 
    #element in the lists is summed up. Different hand types can be distinguished 
    #according to the values of the two sums.
    
    #is_royal_flush:
    # suit_count should be [5,5,5,5,5] ,so sum(suit_count) equals 25
    # value_count should be [1,1,1,1,1],so sum(value_count) equals 5
    # 1st card'value - 5th card'value == 4 
    # 1st card'value == 14
    
    # is_straight_flush:
    # suit_count should be [5,5,5,5,5] ,so sum(suit_count) equals 25
    # value_count should be [1,1,1,1,1],so sum(value_count) equals 5
    # 1st card'value  - 5th card'value == 4 
    # 1st card'value < 14
    
    #is_four_of_a_kind:
    # value_count should be [4,4,4,4,1](order is ignored)
    # so sum(value_count) equals 17
    
    #is_full_house:
    # value_count should be [3,3,3,2,2](order is ignored)
    # so sum(value_count) equals 13
    
    #is_flush:
    # suit_count should be [5,5,5,5,5] ,so sum(suit_count) equals 25
    #  then value_count should not be [1,1,1,1,1],so sum(value_count) != 5
    #       or the hand is not a straight 
   
    #compare method:mainly distinguish the situation where two players rank the same. 
    #With the help of a method that can find five cards that repeat for n times, 
    #find out the pair of two hands, three a kind, four a kind for comparison.
    #compare_highest_card:
    #compare the highest(first) card of two hands
    
    #get_value_repeat:
    #find the cards that repeat n times in the list
    
    #compare_four_of_a_kind:
    #find the four_of_a_kind cards of two hands and compare them
    
    #compare_three_of_a_kind:
    #find the three_of_a_kind card of two hands and compare them
    
    #cmp:
    #compare two numbers
    
    #compare_two_pairs:
    #find the higher pair cards of two hands and compare them
    #while it's a tie find the lower pair cards of two hands and compare them
    #another tie find the single card of two hands and compare them
    
    #compare_one_pair:
    #find the pair cards of two hands and compare them
    #while it's a tie find the highest s
    
#List method and tuple requirements: append, sort, count

class Hand:
    def __init__(self):
        self.hand = []
    
    def get_hand(self):
        return self.hand
    
    def print_hand(self):
        print(f"Hand:{self.hand}")
        
    @staticmethod
    def sorting(card):
        return card.value

    def add_card(self, card):
        self.hand.append(card)
        self.hand.sort(key = Hand.sorting,reverse=True)
    
    def rank(self):
        hand_value = [card.get_value() for card in self.hand]
        hand_suit = [card.get_suit() for card in self.hand]
        if self.is_royal_flush(hand_value,hand_suit):
            return 9
        elif self.is_straight_flush(hand_value,hand_suit):
            return 8
        elif self.is_four_of_a_kind(hand_value):
            return 7
        elif self.is_full_house(hand_value):
            return 6
        elif self.is_flush(hand_value,hand_suit):
            return 5
        elif self.is_straight(hand_value,hand_suit):
            return 4
        elif self.is_three_of_a_kind(hand_value):
            return 3
        elif self.is_two_pair(hand_value):
            return 2
        elif self.is_one_pair(hand_value):
            return 1
        else:
            return 0
            
    def get_card_value(self,i):
        return self.hand[i].value

    def is_royal_flush(self,hand_value,hand_suit):
        suit_count = [hand_suit.count(suit) for suit in hand_suit]
        value_count= [hand_value.count(val) for val in hand_value]
        return sum(suit_count)==25 and sum(value_count)==5 and self.get_card_value(0)-self.get_card_value(4)==4 and self.get_card_value(0)==14
     
    def is_straight_flush(self,hand_value,hand_suit):
        suit_count = [hand_suit.count(suit) for suit in hand_suit]
        value_count= [hand_value.count(val) for val in hand_value]
        return sum(suit_count)==25 and sum(value_count)==5 and self.get_card_value(0)-self.get_card_value(4)==4 and self.get_card_value(0)<14
                
    def is_four_of_a_kind(self,hand_value):
        counts = [hand_value.count(val) for val in hand_value]
        return sum(counts)==17 
    
    def is_full_house(self,hand_value):
        counts = [hand_value.count(val) for val in hand_value]
        return sum(counts)==13
    
    def is_flush(self,hand_value,hand_suit):
        suit_count = [hand_suit.count(suit) for suit in hand_suit]
        value_count= [hand_value.count(val) for val in hand_value]
        return sum(suit_count)==25 and not(sum(value_count)==5 and self.get_card_value(0)-self.get_card_value(4)==4)
    
    def is_straight(self,hand_value,hand_suit):
        suit_count = [hand_suit.count(suit) for suit in hand_suit]
        value_count= [hand_value.count(val) for val in hand_value]
        return sum(value_count)==5 and sum(suit_count)<25 and self.get_card_value(0)-self.get_card_value(4)==4

    def is_three_of_a_kind(self,hand_value):
        counts = [hand_value.count(val) for val in hand_value]
        return sum(counts)==11
    
    def is_two_pair(self,hand_value):
        counts = [hand_value.count(val) for val in hand_value]
        return sum(counts)==9

    def is_one_pair(self,hand_value):
        counts = [hand_value.count(val) for val in hand_value]
        return sum(counts)==7
         
    def get_hand_type(self):
        return rankNames[self.rank()]
    
    def compare(self,other_hand):
        self_rank = self.rank()
        if self_rank>other_hand.rank(): 
            return 1
        elif self_rank<other_hand.rank():
            return -1
        else:
            #Royal Flush - if two hands are both Royal Flushes, it's a true tie.
            if self_rank == 9:
                return 0
            #Straight Flush - the hand with the highest card wins.
            elif self_rank == 8: 
                return self.compare_highest_card(other_hand)
            #Four-of-a-kind - the highest four-of-a-kind value wins, regardless of the value of the 5th card.
            elif self_rank == 7: 
                return self.compare_four_of_a_kind(other_hand)
            #Full House - the highest three-of-a-kind value wins, regardless of the pair values.
            elif self_rank == 6:  
                return self.compare_three_of_a_kind(other_hand)
            #Flush - the hand with the highest card wins.
            elif self_rank == 5: 
                return self.compare_highest_card(other_hand)
            #Straight -  the hand with the highest card wins.
            elif self_rank == 4: 
                return self.compare_highest_card(other_hand)
            #Three-of-a-kind - the highest three-of-a-kind value wins, regardless of the other cards.
            elif self_rank == 3: 
                return self.compare_three_of_a_kind(other_hand)
            #Two Pair - the highest pair value wins. If those are tied, check the second pair. 
            #If those are also tied, check the single card.
            elif self_rank == 2: 
                return self.compare_two_pairs(other_hand)
            #One Pair - the highest pair value wins. If those are tied, compare the highest single card.
            elif self_rank == 1: 
                return self.compare_one_pair(other_hand)
            #High Card - the hand with the highest card wins.
            else: 
                return self.compare_highest_card(other_hand)


    def compare_highest_card(self,other_hand):
        for i in range(0,5):
            if self.get_card_value(i)>other_hand.get_card_value(i):
                return 1
            elif self.get_card_value(i)<other_hand.get_card_value(i):
                return -1
        return 0

#find the cards that repeat n times in the list
    def get_value_repeat(self,n):
        hand_value = [card.get_value() for card in self.hand]
        return [x for x in hand_value if hand_value.count(x)==n]


    def compare_four_of_a_kind(self,other_hand):
        if self.get_value_repeat(4)[0]>other_hand.get_value_repeat(4)[0]:
            return 1
        else: 
            return -1

    def compare_three_of_a_kind(self,other_hand):
        if self.get_value_repeat(3)[0]>other_hand.get_value_repeat(3)[0]:
            return 1
        else: 
            return -1
   
    @staticmethod
    def cmp(x,y):
        if x>y:
            return 1
        elif x<y:
            return -1
        else:
            return 0


    def compare_two_pairs(self,other_hand):
        self_pair = self.get_value_repeat(2)
        other_pair = other_hand.get_value_repeat(2)
        if max(self_pair)>max(other_pair):
            return 1
        elif max(self_pair)<max(other_pair): 
            return -1
        else :
            if min(self_pair)>min(other_pair):
                return 1
            elif min(self_pair)<min(other_pair): 
                return -1
            else : 
                return Hand.cmp(self.get_value_repeat(1)[0],other_hand.get_value_repeat(1)[0])

    def compare_one_pair(self,other_hand):
        self_pair = self.get_value_repeat(2)
        other_pair = other_hand.get_value_repeat(2)
        if self_pair[0]>other_pair[0]:
            return 1
        elif self_pair[0]<other_pair[0]: 
            return -1
        else : 
            return Hand.cmp(self.get_value_repeat(1)[0],other_hand.get_value_repeat(1)[0])

    def get_image(self,is_winner):
        images = [Display.get_image(card) for card in self.hand]
        images.append(Display.text_image(images[0].width,images[0].height,self.get_hand_type(),is_winner))
        return Display.make_row(images)

if __name__ == '__main__':
    poker_game = [Hand() for _ in range(4)]
    deck = Deck.Deck()
    deck.shuffle()
    deck.print_deck()
    for i in range(5):
        print(f"Turn {i}:")
        for player in poker_game:                      
            player.add_card(deck.deal_card())
            player.print_hand()
    for player in poker_game:  
        rank = player.rank()
        print(f"{player.rank()}:{player.get_hand_type()}")
    sum_scores = []
    for i in range(4):
        scores = [poker_game[i].compare(poker_game[j]) for j in range(4) if j!=i]
        print(f"player {i}'s scores:{scores} ")
        sum_scores.append(sum(scores))
    max_score = max(sum_scores)
    winner_indexes = [i for i in range(4) if sum_scores[i]==max_score]
    print(f"player {winner_indexes} is/are the winner/winners ")

    images =[poker_game[i].get_image(sum_scores[i]==max_score) for i in range(4)]
    

    hand1_images = []
    img = Display.make_collum(images)
    img.show()



    