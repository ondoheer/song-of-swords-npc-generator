from modules.character import Character


def run():
    c = Character(race="dwarf")
    c.build_npc()
    print(c)


if __name__ == "__main__":
    run()
