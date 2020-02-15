from modules.character import Character

DEBUG = False
lifestyles = {
    1: "academic",
    2: "criminal",
    3: "civilian",
    4: "military",
    5: "outdoorsman",
    6: "noble",
    7: "merchant",
    8: "medic",
    9: None  # this triggers random
}

races = {
    1: "human",
    2: "dwarf"
}


def set_lifestyle():

    lifestyle = input(f"""
    Choose one of the following lifestyles
    1. Academic
    2. Criminal
    3. Civilian
    4. Military
    5. Outdoorsman
    6. Noble
    7. Merchant
    8. Medic
    9. Random 
       
    """)
    return lifestyle


def set_race():
    race = input(f"""
    Choose one of the following races
    1. Human
    2. Dwarf
     
    """)
    return race


def ask_save_char():
    save = input("Do you want to save it? Y/N ")
    return save.lower()


def save_char(filename, char):
    with open(f"{filename}.txt", "w+") as character:
        character.write(char)


def run():
    """
    Ask if player wants to set a random o specific race and lifestyle
    """
    print(f"""
    -------------------------------
    NPC Builder
    -------------------------------
    """)
    lifestyle_code = 10  # to trigger the while loop

    while int(lifestyle_code) > 9:
        lifestyle_code = int(set_lifestyle())
    lifestyle = lifestyles[lifestyle_code]

    race_code = 10
    while int(race_code) > 9:
        race_code = int(set_race())
    race = races[race_code]
    c = Character(race=race, lifestyle=lifestyle)
    c.build_npc()
    if DEBUG:
        print(c)
    c.print_pc()

    save = " "
    while save not in "yn":
        save = ask_save_char()

    if save == "y":
        filename = input("Enter a name for the file: ")
        save_char(filename, c.get_pc())

    exit()


if __name__ == "__main__":
    run()
