import time

def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, options, errormsg):
    while True:
        response = input(prompt).lower()
        for option in options:
            if response in option:
                return option
        print_pause(errormsg)


def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def pick_floor(items):
    floors = ["first", "second", "third"]
    depart = ["Lobby", "Human Resorces department", "Engineering departmenr"]
    print_pause("Please enter the number for the floor"
                " you would like to visit:")
    floor = int(valid_input("1. Lobby \n"
                            "2. Human Resources \n"
                            "3. Engineering department \n",
                            ["1", "2", "3"],
                            ""))
    print_pause(f"You press the button for the {floors[floor-1]} floor.")
    print_pause(f"After a few moments you find yourself "
                f"in the {depart[floor-1]}.")

    if floor == 1:
        lobby(items)
        print_pause("You head back to the elevator.")
    elif floor == 2:
        humres(items)
        print_pause("You head back to the elevator.")
    elif floor == 3:
        engine(items)


def lobby(items):
    print_pause("You are greeted by the clerk.")
    if "id_card" in items:
        print_pause("He has already given you your ID card")
    else:
        items.append("id_card")
        print_pause("He signs you in and gives you your ID card")
    head_back(items)


def humres(items):
    if "handbook" in items:
        print_pause("The HR folks are busy at their desks")
        print_pause("There dosen't seem to be much to do here.")
        head_back(items)

    print_pause("You are greeted by the head of HR.")
    if "id_card" in items:
        items.append("handbook")
        print_pause("She looks at your ID card then gives you a copy"
                    " of the employee handbook")
    else:
        print_pause("She has something for you, but you need something"
                    " else first.")
    head_back(items)


def engine(items):
    print_pause("This is where you work!")
    if "id_card" not in items:
        print_pause("Unfortunately The door is locked.")
        print_pause("It looks like you need some kind of keycard"
                    " to open the door.")
        head_back(items)
    print_pause("You use your ID card to open the door.")
    print_pause("The Program manager greets you and tells you that"
                " you need a handbook before you can start work")
    if "handbook" in items:
        print_pause("Fortunately you got that from HR")
        print_pause("Congratulations! You are ready to start your new"
                    " job as vice president of engineering!")
        quit()            
    else:
        print_pause("They scowl when they see you don't have it, "
                    "and send you back to the elevator")
        pick_floor(items)


def head_back(items):
    print_pause("You head back to the elevator")
    pick_floor(items)


def Elevatorgame():
    items = []
    intro()
    pick_floor(items)


Elevatorgame()
