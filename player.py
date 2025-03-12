import json
from spell import *

class Player:
    def __init__(self, name, school, lvl):
        self.name = name
        self.school = school
        self.lvl = lvl
        self.spellbook = []
        self.gear_mod = 1

        self.fill_spellbook()
        self.check_spellbook()

        self.offense_stack = Magic_Stack()
    
    def fill_spellbook(self):
        #get all spells from database and add death spells
        with open('database.json', 'r') as file:
            data = json.load(file)
        
        runes = data['spells']
        for rune in runes:
            if (rune['school'] == self.school) and (rune['lvl_learned'] <= self.lvl):
                if rune['type'] == "Attack":
                    min_damage = rune['min_damage']
                    max_damage = rune['max_damage']
                else :
                    min_damage = 0
                    max_damage = 0
                self.spellbook.append(Spell(rune['name'], rune['school'], rune['pip_cost'], rune['accuracy'], rune['type'], rune['lvl_learned'], rune['target'], rune['buff'], rune['description'], min_damage, max_damage))
    
    def check_spellbook(self):
        print("This wizard has the following spells at his disposal:")
        for page in self.spellbook:
            print(page.name)

    # def cast_spell(self, spell):
    #     if spell.type == "Charm":
    #         self.cast_charm(spell)
    #     elif spell.type == "Attack":
    #         self.cast_attack(spell, target)

#cast a buffing spell to add to your stack
    def cast_charm(self, charm):
        self.offense_stack.add_spell(charm)
        print(f"You casted a {charm.name}!")

#cast an attack at enemy object
    def cast_attack(self, attack, target):
        minimum, maximum = self.offense_stack.cast_stack(attack, target)
        print(f"Your {attack.name} will deal between {minimum}-{maximum} damage to the {target.name}")
