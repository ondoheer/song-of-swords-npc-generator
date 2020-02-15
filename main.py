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


def yes_no(action):
    save = input(f"Do you want to {action}? Y/N ")
    return save.lower()


def save_char(filename, char):
    with open(f"{filename}.txt", "w+") as character:
        character.write(char)


def split_text(text, position):
    """
    splits a one line text string into many lines 
    adding a new line character at position
    """
    new_text = ""
    text_len = len(text)
    # last line doesn't need a new line symbol
    lines_to_break = text_len // position - 1
    broken_lines = 0
    new_position = position
    while broken_lines <= lines_to_break:
        break_attempt = text[position]
        while break_attempt != " ":
            new_position = new_position + 1
            break_attempt = text[new_position]
        new_text += "\t" + text[:new_position] + "\n"
        text = text[new_position:]
        broken_lines += 1
    new_text += "\t" + text
    return new_text


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

    # write background
    write_background = yes_no("write this characters background")
    if write_background == "y":
        background = input(
            "Write the background here, careful, the Enter key stops this process, don't get exited\n")
        formated_background = split_text(background, 64)
        c.add_background_story(formated_background)
        c.print_pc()
    # save the NPC
    save = " "
    while save not in "yn":
        save = yes_no("save it")

    if save == "y":
        filename = input("Enter a name for the file: ")
        save_char(filename, c.get_pc())

    # prompt to create another NPC
    create_other = yes_no("create another character")
    if create_other == "y":
        run()
    else:
        exit()


if __name__ == "__main__":
    run()
