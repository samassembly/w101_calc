def print_options(options):
    print("Please choose an option:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

schools = ["Pyromancy", "Divination", "Thaumaturgy", "Conjuration", "Theurgy", "Necromancy", "Sorcery"]
print_options(schools)