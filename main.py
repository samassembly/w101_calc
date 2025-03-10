from spell import Spell

def main():
    print("Creating a Deathblade")
    new_spell = Spell("Deathblade", "Death", 0, 1.00, "Charm", 7, "Self", 0.35, "Applies a 35% Death Damage or Steal Charm")

    print("What does Deathblade do again?")
    print(new_spell.help())

if __name__ == "__main__":
    main()