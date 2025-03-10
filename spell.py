import math

class Spell:
    def __init__(self, name, school, pip_cost, accuracy, charm, lvl_learned, target, buff, description, min_damage = 0, max_damage = 0):
        self.name = name
        self.school = school
        self.pip_cost = pip_cost
        self.accuracy = accuracy
        self.type = charm
        self.lvl_learned = lvl_learned
        self.target = target
        self.buff = buff
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.description = description
    
    def help(self):
        return self.description

class Magic_Stack:
    def __init__(self):
        self.stack = []
        self.multiplier = 1
    
    def add_spell(self, spell):
        (self.stack).append(spell)

    def cast_stack(self, casted_spell):
        #FIFO resolve status, all unique casts get added to modifiers
        cast_school = casted_spell.school
        resolved_spells = []
        for i in range(len(self.stack)):
            #make sure spell hasn't bene resolved and it the correct type
            if (self.stack[i].school == cast_school):
                #overall multiplier adjustments
                self.multiplier *= (1 + self.stack[i].buff)
                #add spell to resolved so it doesn't get added again
                resolved_spells.append(self.stack[i])
        for j in range(len(resolved_spells)):
            (self.stack).remove(resolved_spells[j])
        min_damage = math.ceil(casted_spell.min_damage * self.multiplier)
        max_damage = math.ceil(casted_spell.max_damage * self.multiplier)
        return min_damage, max_damage
    
    def check_stack(self):
        for spell in self.stack:
            print(spell.name)