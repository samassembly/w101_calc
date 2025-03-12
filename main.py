from spell import *
from player import *
from enemy import *

def main():

    print("Summoning Lost Soul to fight!")
    first_enemy = Enemy("Lost Soul", 1, 55, "Undead", "Death", 1, 0, 0, True, True)
    print(first_enemy.help())
    print()

    print("Requesting assistance from Grandmaster Necromancer, Samuel Shadowsong!")
    death_student = Player("Samuel Shadowsong", "Death", 164)
    print()
    casting_time = True

    while casting_time:
        selection = input("What spell would you like to cast: ")
        for spell in death_student.spellbook:
            if spell.name == selection:
                if spell.type == "Charm":
                    death_student.cast_charm(spell)
                elif spell.type == "Attack":
                    death_student.cast_attack(spell, first_enemy)
        # print("Spell not found, pick another!")
            

    

if __name__ == "__main__":
    main()