'''
Created on Apr 4, 2023

@author: limuyang
'''
names = ("2", "3","4","5","6","7","8", "9","10", "jack","queen","king","ace")

# Class model: Card
# The attributes: value and suit 
# Major algorithms implemented: None
#List method and tuple requirements: None
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return self.get_name()

    def get_value(self):
        return self.value
        
    def get_suit(self):
        return self.suit
    
    def get_name(self):
        return f"{names[self.value-2]} of {self.suit}"
    
    def image_file_name(self):
        return f"{names[self.value-2]}_of_{self.suit}.png"

