import json
from spell import Spell

class Player:
    def __init__(self, name, school, lvl):
        self.name = name
        self.school = school
        self.lvl = lvl
        self.spellbook = []
    
    def fill_spellbook(self):
        #get all spells from database and add death spells
        with open('database.json', 'r') as file:
            data = json.load(file)
        
        runes = data['spells']
        for rune in runes:
            if rune['school'] == self.school:
                if rune['type'] == "Attack":
                    min_damage = rune['min_damage']
                    max_damage = rune['max_damage']
                else :
                    min_damage = 0
                    max_damage = 0
                self.spellbook.append(Spell(rune['name'], rune['school'], rune['pip_cost'], rune['accuracy'], rune['type'], rune['lvl_learned'], rune['target'], rune['buff'], rune['description'], min_damage, max_damage))
    
    def check_spellbook(self):
        for page in self.spellbook:
            print(page.name)