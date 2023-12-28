import random
import time

def Hero_Game():  # This runs the whole game!  # (STEP 3)
    # Randomly assigns either a 1 or a 0 to the values of each weapon
    int_arrow = random.randint(0, 1)
    int_sword = random.randint(0, 1)
    int_magic = random.randint(0, 1)
    int_hammer = random.randint(0, 1)
    coin_count = 8  # Player starting coin count
    Hero_health = 3  # Player starting health
    round_number = 1  # Starting round number
    like_to_buy = "n"  # This sets the like to buy variable to no for future use
    # Inventory is very important and all the data above is stored in a list that the player will access and manipulate in the game.
    inventory = [int_arrow, int_sword, int_magic, int_hammer, coin_count, Hero_health, like_to_buy, round_number]
    monsters_killed = []
    monsters = {
        "Dragon": "1",
        "Zombie": "2",
        "Ghost": "3",
        "Minotaur": "4",
        "Dragon ": "1",
        "Zombie ": "2",
        "Ghost ": "3",
        "Minotaur ": "4"
    }  # This is a dict of monsters; there is one duplicate of every monster

    while True:  # Asks the user for a difficulty till they enter 1, 2, or 3 and repeats the questions till they do.  # (STEP 4)
        difficulty_level = (input('Select difficulty: Easy = "1", Normal = "2", Hard = "3": '))
        if difficulty_level == "1" or difficulty_level == "2":
            break
        elif difficulty_level == "3":
            coin_count -= 2
            break
        else:
            print("Try that again!")

    print("Loading", end="")  # I thought it would be nice to embellish the game with a loading screen.
    time.sleep(1)  # I used the time module throughout the game to enhance the UI.
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("1. To protect our town you must select the correct weapons to defeat the monsters that are attacking! ")
    time.sleep(3)
    print("2. If you are struck by a monster you will lose 1 health. Use your weapons carefully.")
    time.sleep(3)
    print("3. If you encounter a monster and you don't have any weapons, you will DIE!")
    time.sleep(3)
    print("4. You can use coins to buy weapons: weapon cost = 1")
    time.sleep(3)
    print("5. Earn 1 coin every time you kill a monster!")
    time.sleep(3)

    def current_inventory():  # This function will always print the current inventory
        print(f"Hero's Arsenal: Sword: ({inventory[0]} uses left) ", end="")
        print(f"Arrow: ({inventory[1]} uses left) ", end="")
        print(f"Magic: ({inventory[2]} uses left) ", end="")
        print(f"Hammer: ({inventory[3]} uses left) ")
        time.sleep(0.5)
        print(f"Coin(s): {inventory[4]}")
        time.sleep(0.5)
        print(f"Health: {inventory[5]}")
        time.sleep(0.5)

    current_inventory()

    def Shop(inventory):  # This is a shop function allowing the player to exchange coins for weapons
        if inventory[6] == 'y':  # Skips the shop if the player does not want to buy anything
            def purchasing_process(index_of_item):
                inventory[index_of_item] += 1
                inventory[4] -= 2
                print("Counting coins")
                time.sleep(1)
                print("Purchasing!")
                time.sleep(1)
                current_inventory()
                print("________________________________________________________________")
                print()

            def not_enough_coins():  # Prints a message if the player doesn't have enough coins
                print("Counting coins")
                time.sleep(3)
                print("You don't have enough money for that!")
                time.sleep(1)
                print("Thanks for shopping!")

            while True:  # This while loop will ask the player if they would like to buy until the player is done purchasing.
                # Each block of if statements checks the desired weapon and the coin amount before proceeding.
                Which_Weapon = input('Which weapon would you like to buy? Arrow: "1", Sword: "2", Magic: "3", Hammer: "4" Finished: enter anything')
                if Which_Weapon == "1":
                    if inventory[4] > 1:
                        purchasing_process(0)
                    else:
                        not_enough_coins()
                        break

                if Which_Weapon == "2":
                    if inventory[4] > 1:
                        purchasing_process(1)
                    else:
                        not_enough_coins()
                        break

                if Which_Weapon == "3":
                    if inventory[4] > 1:
                        purchasing_process(2)
                    else:
                        not_enough_coins()
                        break

                if Which_Weapon == "4":
                    if inventory[4] > 1:
                        purchasing_process(3)
                    else:
                        not_enough_coins()
                        break

                elif Which_Weapon != "1" and Which_Weapon != "2" and Which_Weapon != "3" and Which_Weapon != "4":
                    print("Thanks for shopping!")
                    time.sleep(1)
                    current_inventory()
                    break
        else:
            pass

    def New_round(monsters, inventory):  # This runs the heart of the game or the rounds the player must pass.  # (STEP 6)
        print("________________________________________________________________")
        print()
        print(f"Round Number: {inventory[7]} Starting", end="")
        time.sleep(0.5)
        print(".", end="")
        time.sleep(0.5)
        print(".", end="")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        current_inventory()
        time.sleep(1)
        print("________________________________________________________________")
        random_Monster = random.choice(list(monsters.keys()))
        print(f"A Wild {random_Monster} Appears!")
        print("Which weapon will you choose? ")

        def winning_process(index_of_weapon, random_Monster):  # This function runs if the player makes a correct weapon selection
            print("CLASH  ", end="")
            time.sleep(2)
            print("BANG  ", end="")
            time.sleep(2)
            print("ZING")
            time.sleep(2)
            inventory[index_of_weapon] -= 1  # Subtracts one use of the player's weapon
            del monsters[random_Monster]  # Delete the monster the player defeated from the dict of monsters
            monsters_killed.append(random_Monster)  # Add the monster to a list of defeated monsters
            inventory[7] += 1  # Adds a coin to their inventory
            inventory[4] += 1  # Adds a round to the count of rounds.
            print(f"You have slain {random_Monster} and earned a coin")
            print(f"Coin(s): {inventory[4]}")

        def wrong_weapon(index_of_weapon, random_Monster):  # This function runs if the player has the weapon but it is an incorrect selection.
            print(f"Wrong Weapon! {random_Monster} is immune!")
            inventory[index_of_weapon] -= 1
            inventory[5] -= 1
            print(f"Health Left: {inventory[5]}")

        def death_process(random_Monster):  # If the player is out of the weapon they selected, they are facing a monster
            # barehanded and will unfortunately lose their health
            print(f"You are out of that weapon! The {random_Monster} has eaten you!")
            inventory[5] = 0

        while True:  # This while loop runs the round/player's weapon selection.
            # The if statements are checking if the selected weapon will kill the random monster and if the
            # player has enough health left
            if inventory[5] > 0:
                weapon_select = input('Select: Arrow: "1", Sword: "2", Magic: "3", Hammer: "4" : ').lower()

                if weapon_select == "1":
                    if inventory[0] != 0:
                        if monsters.get(random_Monster) == weapon_select:
                            winning_process(0, random_Monster)
                            break
                        else:
                            wrong_weapon(0, random_Monster)
                    else:
                        death_process(random_Monster)

                elif weapon_select == "2":
                    if inventory[1] != 0:
                        if monsters.get(random_Monster) == weapon_select:
                            winning_process(1, random_Monster)
                            break
                        else:
                            wrong_weapon(1, random_Monster)
                    else:
                        death_process(random_Monster)

                elif weapon_select == "3":
                    if inventory[2] != 0:
                        if monsters.get(random_Monster) == weapon_select:
                            winning_process(2, random_Monster)
                            break
                        else:
                            wrong_weapon(2, random_Monster)
                    else:
                        death_process(random_Monster)

                elif weapon_select == "4":
                    if inventory[3] != 0:
                        if monsters.get(random_Monster) == weapon_select:
                            winning_process(3, random_Monster)
                            break
                        else:
                            wrong_weapon(3, random_Monster)
                    else:
                        death_process(random_Monster)
            else:
                break

    for i in range(int(difficulty_level) * 2):  # This for loop runs the appropriate amount of rounds depending on the user's
        # difficulty level. It will end the game if the player dies.  # (STEP 5)
        if inventory[5] <= 0:
            print("________________________________________________________________")
            print()
            print("You have died! GAME OVER")
            break
        else:
            inventory[6] = input("Would you like to buy anything from the shop? (Y/N) ")
            Shop(inventory)
            New_round(monsters, inventory)
    if inventory[5] > 0:
        print()
        print("Thank you Hero! You saved us! ")
        time.sleep(1)
        print()
        print("You killed: " + '1. '.join(monsters_killed))
        time.sleep(1)
    start_game(input("Would you like to start a new game? (Y/N)").lower())


def start_game(startGame):  # This function will start the game!  # (STEP 2)
    if startGame == "y":
        Hero_Game()
    elif startGame == "n":
        print("Have a good day!")
    else:
        print("Oops, something went wrong. Try again")


start_game(input("Would you like to start a new game? (Y/N)").lower())  # (STEP 1)