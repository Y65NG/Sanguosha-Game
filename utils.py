
class Basic:
    def __init__(self):
        pass

    def attack(self, this, other):
        other.hp -= 1
        return True
    
    def defend(self, this, other):
        pass