
def play_game():
    user=0
    while user==0:
        play = input("Welcome to stabby stabby orc game. Would you like to play? Y/N ")
        if play.lower() == "n" or play.lower() == "no":
            user=1
            print("Goodbye.")
        elif play.lower() == "y" or play.lower() == "yes":
            user=1
            game()
        else:
            print("Try and enter a valid input.")


def game():
    orc_health = 100
    import random
    us_health = random.randint(50, 100)
    print("ORC: GRR I AM AN ANGRY ORC I WILL KILL YOU!")
    print("Your health is:", us_health)
    weapons()


def weapons(weapon):
    weapons_names = [["Knuckle Dusters", 45],
                     ["Dagger"],
                     ["Mystery Potion"]]
    if weapon not in weapons_names:
        return 1
    return 0


def main():
    play_game()
    my_weapon = input("What weapon will you choose? ")
    valid_weapon = weapons(my_weapon)



main()
