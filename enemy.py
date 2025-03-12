class Enemy:
    def __init__(self, name, rank, health, classification, school, starting_pips, incoming_boost, incoming_resist, stunnable, beguilable):
        self.name = name
        self.rank = rank
        self.health = health
        self.classification = classification
        self.school = school
        self.starting_pips = starting_pips
        self.incoming_boost = incoming_boost
        self.incoming_resist = incoming_resist
        self.stunnable = stunnable
        self.beguilable = beguilable

        self.defense_stack = []

    def help(self):
        output = f"A {self.name} is a {self.classification} of rank {self.rank}. They start combat with {self.health} health."
        return output

    def get_wards(self):
        for ward in self.defense_stack :
            print(ward.name)
        
    def get_charms(self):
        for charm in self.offense_stack:
            print(charm.name)

    def cast_ward(self, ward):
        self.defense_stack.append(ward)
        print(f"{self.name} cast a protective {ward.name}!")

    def cast_charm(self, charm):
        self.offense_stack.append(charm)
        print(f"{self.name} cast a buffing {charm.name}!")

    def check_stack(self, stack):
        print(f"{self.name} has the following active spells:")
        for spell in stack:
            print(spell.name)