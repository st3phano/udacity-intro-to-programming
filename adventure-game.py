import time
import random


def print_pause(message):
    print(message)
    time.sleep(.5)


def validate_input(message, options):
    while True:
        choice = input(message)
        if choice in options:
            return choice


def intro(monster):
    print_pause("You find yourself in an open field.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold a not very effective dagger.")


def house(monster, weapon, cave_weapon):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {monster}!")
    print_pause(f"The {monster} attacks you!")

    if "dagger" == weapon:
        print_pause("You feel a bit under-prepared for this "
                    "only having a tiny dagger.")

    options = ['f', 'r']
    choice = validate_input("Would you like to (f)fight or (r)run away?\n",
                            options)

    if 'f' == choice:
        if "dagger" == weapon:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {monster}.")
            print_pause("You have been defeated!")
        else:
            print_pause(f"As the {monster} moves to attack, "
                        f"you raise your {weapon}.")
            print_pause(f"The {weapon} shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {monster} takes one look "
                        "at your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {monster}. "
                        "You are victorious!")
    else:
        print_pause("You run back into the field. "
                    "Luckily, you don't seem to have been followed.")
        field(monster, weapon, cave_weapon)


def cave(monster, weapon, cave_weapon):
    print_pause("You peer cautiously into the cave.")

    if "dagger" == weapon:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock...")
        print_pause(f"You have found the {cave_weapon}!")
        print_pause("You discard your silly old dagger "
                    "and take your brand new weapon with you.")
        weapon = cave_weapon
    else:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")

    print_pause("You walk back out to the field.")
    field(monster, weapon, cave_weapon)


def field(monster, weapon, cave_weapon):
    options = ['h', 'c']
    choice = validate_input("\nWhich way do you want to go?\n"
                            "Enter 'h' to knock on the door of the house.\n"
                            "Enter 'c' to peer into the cave.\n", options)

    if 'h' == choice:
        house(monster, weapon, cave_weapon)
    else:
        cave(monster, weapon, cave_weapon)


def play_again():
    options = ['y', 'n']
    choice = validate_input("Would you like to play again? (y/n)\n", options)

    if 'y' == choice:
        print_pause("\nRestarting the game...\n")
        return True
    else:
        return False


def game_loop():
    playing = True
    while playing:
        monsters = ["lizard", "troll", "witch", "minotaur"]
        monster = random.choice(monsters)

        weapon = "dagger"
        cave_weapons = ["magic long sword", "sollar axe", "mortal mace"]
        cave_weapon = random.choice(cave_weapons)

        intro(monster)
        field(monster, weapon, cave_weapon)
        playing = play_again()
    print("Thanks for playing!")


if __name__ == "__main__":
    game_loop()
