STATES = ['Normal', 'Attacked', 'Predead', 'Dead']

class Player:
    def __init__(self, name, id, general):
        self.name = name
        self.id = id
        self.general = general
        self.hp = self.general.max_hp
        self.hands = []
        self.state = STATE[0]
    
    
    
        