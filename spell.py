class Spell:
    def __init__(self, name, school, pip_cost, accuracy, charm, lvl_learned, target, buff, description):
        self.name = name
        self.school = school
        self.pip_cost = pip_cost
        self.accuracy = accuracy
        self.type = charm
        self.lvl_learned = lvl_learned
        self.target = target
        self.buff = buff
        self.description = description
    
    def help(self):
        return self.description