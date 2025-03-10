from spell import *
from player import *

def main():
    curr_stack = Magic_Stack()

    death_blade = Spell("Deathblade", "Death", 0, 1.00, "Charm", 7, "Self", 0.35, "Applies a 35% Death Damage or Steal Charm")
    dark_sprite = Spell("Dark Sprite", "Death", 1, 0.85, "Attack", 1, "Enemy", 0, "Deals 65-105 Death Damage", 65, 105)
    life_blade = Spell("Lifeblade", "Life", 0, 1.00, "Charm", 0, "Self", 0.35, "Applies a 35% Life Damage Charm")

    print("Casting a Deathblade...")
    curr_stack.add_spell(death_blade)
    print("Casting a Lifeblade...")
    curr_stack.add_spell(life_blade)



    print("Casting a Dark Sprite!")
    min, max = curr_stack.cast_stack(dark_sprite)
    print(f"You will deal between {min} and {max} to the target.")

    print("What is left on the stack: ")
    curr_stack.check_stack()

    print("Creating famed Necromancer, Samuel ShadowSong!")
    death_student = Player("Samuel ShadowSong", "Death", 164)
    print("Retrieving a Master Necromancer Spellbook...")
    death_student.fill_spellbook()
    print("The following spells are in the spellbook:")
    death_student.check_spellbook()
    

if __name__ == "__main__":
    main()