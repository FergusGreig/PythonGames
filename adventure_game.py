import time
import random
import game_aspects


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, options, errormsg):  # validate answers
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return option
        print_pause(errormsg)


def intro(things):  # Opening statements
    print_pause("You arrive into a strange town on horseback.")
    print_pause("Tired from your travels you stable your horse "
                "and head to the local tavern.")
    print_pause("Some locals see you alone and invite you over for a drink.")
    drink(things)
    print_pause("You decide to investigate in the morning.")
    print_pause("...")
    print_pause("You awake with a heavy head and head outside.")


def drink(things):  # Decides ending 1 = drunken fool, 2 = princess
    things['stay'] = valid_input("Do you (1) join them or (2) "
                                 "call it a night?\n",
                                 ["1", "2"], "That wasn't an option!")
    if things['stay'] == "1":
        print_pause("You stay for a drink")
    else:
        print_pause("You politely decline and get up to leave when the barte"
                    "nder offers you a free drink and reccomends you stay.\n")
    print_pause(f"After gaining the locals trust with a story about a "
                f"werewolf they inform you that a {things['monstername']}"
                " has kidnapped a princess and that there is a handsome"
                " reward for their safe return")
    time.sleep(3)


def town(things):
    time.sleep(2)  # Extra wait time to imply travel
    print_pause(f"You are in the town square, you are wearing your "
                f"{things['clothname']}, and have"
                f" your {things['wpnname']} sheathed at your side")
    print_pause("You check a nearby signpost.")
    # Display options
    print_pause("\nHead North to get to the old forest\n"
                "Head East to investigate the cave\n"
                "Head West to check out the castle\n"
                "Head South to visit the beach\n")
    direction = valid_input("Where will you go?\n",
                            ['north', 'east', 'south', 'west'],
                            "Please enter a direction")
    # Relocate
    if direction == 'north':
        forest(things)
    elif direction == 'east':
        cave(things)
    elif direction == 'west':
        castle(things)
    elif direction == 'south':
        beach(things)


def forest(things):  # Monster = Ent, item = weapon
    print_pause("You walk into the forest.")
    print_pause("The air is humid and alive with animal noises.")
    if things['monstername'] == 'Ent':
        print_pause("You hear someone yelling from the tree tops.")
        print_pause("Suddenly you get knocked off your feet by a branch.")
        fight(things)
    else:
        print_pause("There dosent seem to be anyone around.")
        print_pause("You spy something stuck in a tree and "
                    "walk over to investigate.")
        makesword(things)
    town(things)


def cave(things):  # Monster = Troll, item = armour
    print_pause("You clamber into the cave.")
    print_pause("It's very dark and the air is chilled.")
    if things['monstername'] == 'Troll':
        print_pause("You hear someone sobbing up ahead.")
        print_pause("You stub your toe an a rock and trip backwards over a "
                    "boulder which wasn't there before.")
        fight(things)
    else:
        print_pause("There dosent seem to be anyone around.")
        print_pause("You step in a puddle and hear a clang, after a moments"
                    " groping you uncover some armor.")
        makecloth(things)
    town(things)


def castle(things):  # Monster = Vampire, item = weapon
    print_pause("You walk up to the castle and in through an open door.")
    print_pause("The door closes behind you with an ominous creek.")
    if things['monstername'] == 'Vampire':
        print_pause("You hear some whispering up ahead.")
        print_pause("You get acosted by a swarm of bats and fall to your"
                    " knees to protect your face.")
        fight(things)
    else:
        print_pause("There dosent seem to be anyone around.")
        print_pause("You wander aimlessly before stumbling upon a "
                    "weapon displayed on the wall.")
        makesword(things)
    town(things)


def beach(things):  # Monster = Kraken, item = armour
    print_pause("You trek over to the beach.")
    print_pause("The sun is shining and the waves are crashing "
                "gently against the sand.")
    if things['monstername'] == 'Kraken':
        print_pause("You see a figure out to sea, waving frantically.")
        print_pause("Suddenly, an almighty wave sweeps you up the shore.")
        fight(things)
    else:
        print_pause("There dosent seem to be anyone around.")
        print_pause("Squinting your eyes against the sun, you can make out a"
                    " shape amongst the driftwood.")
        makecloth(things)
    town(things)


def makesword(things):
    # Generate weapon
    wpntype = random.choice(game_aspects.weapons)
    embellish = random.choice(game_aspects.embelishment)
    element = random.choice(game_aspects.elements)
    damage = random.randint(2, 12)
    name = f"{element} {wpntype} of {embellish}"
    print_pause(f"It's the {name}!!")
    # Indicate strength
    if damage <= 5:
        quality = "Rather blunt!"
    elif damage < 10:
        quality = " quite sharp."
    else:
        quality = "very sharp!"
    print_pause(f"It looks {quality}")
    # Ask if wanted
    if valid_input("Do you take it?\n",
                   ['y', 'n'], 'Please enter y or n') == 'y':
        print_pause(f"Discarding your {things['wpnname']} you take "
                    f"the {name} and head back to town")
        things['wpnname'] = name
        things['wpnelmnt'] = element
        things['wpndmg'] = damage
    else:
        print_pause(f"You leave the {name} where it is and head back to town")


def makecloth(things):
    # Generate armour
    clothtype = random.choice(game_aspects.cloth)
    embellish = random.choice(game_aspects.embelishment)
    element = random.choice(game_aspects.strategy)
    defense = random.randint(2, 12)
    name = f"{element} {clothtype} of {embellish}"
    print_pause(f"It's the {name}!!")
    # Indicate quality
    if defense <= 5:
        quality = "made of scrap."
    elif defense < 10:
        quality = "old but well constructed."
    else:
        quality = "brand new!"
    print_pause(f"It looks like it is {quality}")
    # Ask if it is wanted
    if valid_input("Do you take it?\n",
                   ['y', 'n'], 'Please enter y or n') == 'y':
        print_pause(f"Discarding your {things['clothname']} you take "
                    f"the {name} and head back to town.")
        # Assign new armour
        things['clothname'] = name
        things['clothstrat'] = element
        things['clothdef'] = defense
    else:
        print_pause(f"You leave the {name} where it is and head back to town.")


def fight(things):
    print_pause("You leap back to your feet and see before you a fearsome"
                f" {things['monstername']}.")
    # Odds values determines outcome. Includes your health, monster health
    # weapon and armor values and type advantages.
    odds = things['yourhp'] - things['monsterhp']
    odds += things['clothdef'] + things['wpndmg']
    if things['clothstrat'] == things['monsterstrat']:
        odds += 10
    if things['wpnelmnt'] == things['monsterweak']:
        odds += 10
    # Indicate chance of victory
    if odds < -5:
        print_pause('It looks invincible.')
        win = False
        hard = False
    elif odds > 5:
        print_pause("It looks like a pushover.")
        win = True
        hard = False
    else:
        print_pause("It looks like it will be a fair match.")
        win = random.choice([True, False])
        hard = True
    # Fight or Flight
    if valid_input("Do you (1) stay and fight or (2) run like hell?\n",
                   ['1', '2'], "Please enter 1 or 2.") == '2':
        print_pause("You turn tale and flee back to town.")
        town(things)
    elif win:  # Winning the game
        if hard:
            print_pause("After a long and gruelling battle you eventually"
                        f" defeat the {things['monstername']} with a mighty "
                        f"strike from the {things['wpnname']}.")
        else:
            print_pause(f"You draw the {things['wpnname']} and "
                        f"eliminate the {things['monstername']} with a "
                        "single blow.")
        outtro(things)  # Go to ending
    else:  # Death
        if hard:
            print_pause(f"You attack the {things['monstername']} with your "
                        f"{things['wpnname']} and deal some hefty damage.")
            print_pause(f"Unfortunately you lose your {things['clothname']}"
                        " to a glancing blow and are left defenceless")
        else:
            print_pause(f"The {things['monstername']} sees you and laughs at your "
                       f"{things['wpnname']} and your {things['clothname']}.")
        print_pause(f"The {things['monstername']} then attacks you with"
                    " all its strength killing you in a very gruesome way.")
        play_again()


def outtro(things):
    if things['stay'] == '2':  # Princess ending
        print_pause(f"As you stand by the slain {things['monstername']} "
                    "a young lady approaches you.")
        print_pause("She is extremely grateful to you for saving her.")
        print_pause("You both head to the town where word has already arrived"
                    " of this heroic deed and a large party has begun.")
        print_pause("You are greeted by the King and Queen who, as a token of"
                    " their thanks, offer you the Princessess"
                    " hand in marriage.")
        if valid_input("Do you 1) respectfully decline or 2) "
                       "graciously accept? \n",
                       ['1', '2'], "Please enter 1 or 2.") == 1:
            print_pause("The king takes this a grave insult "
                        "and has you beheaded.")
        else:
            print_pause("You get married that same day and ride "
                        "off into the sunset.")
            print_pause("And there was much rejoicing.")
    elif things['stay'] == '1':  # Drunken fool ending
        print_pause(f"As you stand by the slain {things['monstername']} "
                    "a bedraggled man approaches you.")
        print_pause("He is extremly gratefull to you for saving him.")
        print_pause(f"He says one minute he is happily drinking in the tavern"
                    f", the next he is being held captive by a "
                    f"{things['monstername']}.")
        print_pause("Determined to get to the bottom of this you both head "
                    "back to the tavern.")
        print_pause("Upon arrival you are greeted with cheers"
                    " from the locals.")
        print_pause("They say that it started out as joke "
                    "but quickly got out of hand.")
        print_pause("As an appology for the inconvienince "
                    "they offer to buy you a pint.")
        if valid_input("Do you 1) take the pint and laugh it off or 2) "
                       "decline the pint and start a fight.\n", ['1', '2'],
                       "Please enter 1 or 2") == '2':
            print_pause(f"It turns out your {things['wpnname']} and "
                        f"{things['clothname']} are no match for a"
                        " group of drunken brawlers.")
            print_pause("Your bleeding corpse is fed to"
                        " the pigs in the morning.")
        else:
            print_pause("You have a good time with everyone in the tavern.")
            print_pause("In the morning you ride off looking for "
                        "your next adventure.")
    play_again()


def play_again():  # End of game and reply
    print_pause("The game is now over.")
    if valid_input("Would you like to play again?\n",
                   ['y', 'n'], "Please enter yes or no") == 'y':
        run_game()
    else:
        quit()


def run_game():
    # Generate monster
    monster = random.choice(game_aspects.monsters)
    # Set up dictionary of things relevent to the game
    things = {'monstername': monster[0], 'monsterweak': monster[1],
              'monsterstrat': monster[2], 'monsterhp': random.randint(25, 40),
              'wpnname': "Blunt knife", 'wpnelmnt': "none", 'wpndmg': 1,
              'clothname': "Riding shirt", 'clothstrat': "none",
              'clothdef': 1, 'yourhp': 10, 'stay': '1'}
    intro(things)
    town(things)


# Begin.
if __name__ == "__main__":
    run_game()
