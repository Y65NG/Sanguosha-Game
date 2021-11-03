import random as rd

SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
G_SKILLS = {}
BASIC_CARDS = {'Attack': , 'Defend': }
WEAPON_CARDS = {}



class Card:
    def __init__(self, suit, point, name):
        self.suit = suit
        self.point = point
        self.name = name
    
    def __str__(self):
        return self.suit + ' ' + self.point + ' ' + self.name

class GeneralCard(Card):
    def __init__(self, suit, point, name, max_hp):
        super().__init__(suit, point, name)
        self.skills = G_SKILLS[name]
        self.max_hp = max_hp
    
    def skill(self, ski_name):
        return self.skills[ski_name]
    
class BasicCard(Card):
    def __init__(self, suit, point, name):
        super().__init__(suit, point, name)
    
    def use(self):
        return BASIC_CARDS[self.name]

class WeaponCard(BasicCard):
    def __init__(self, suit, point, name):
        super().__init__(suit, point, name)
        
    def use(self):
        return WEAPON_CARDS[self.name]



        