from modules.character import Character

DEBUG = False


def run():
    c = Character(race="dwarf")
    c.build_npc()
    if DEBUG:
        print(c)
    c.print_pc()


if __name__ == "__main__":
    run()
