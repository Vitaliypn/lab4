import lviv_game
from random import randint

print("""
Welcome to the Lviv game. Your task here will be to go
to Kozelnytska street. Be careful and never go back only forward.
There will be several enemies and u need to worry not to be killed""")


street1 = lviv_game.Room("Краківська")
street1.set_description("You bus stop here and u need to get to Kolegium.")

street2 = lviv_game.Room("проспект Тараса Шевченка")
street2.set_description("Here you can meet gopnik be careful")
gopnik = lviv_game.Gopnik('Gopnik','A guy that likes to were adidas', 6, randint(1,6))
street2.set_character(gopnik)

street3 = lviv_game.Room("вулиця Стрийська")
street3.set_description("Be carefull here can be soldiers")
soldier = lviv_game.Soldier('Soldier','A guy that can give u a notice', 8, 10000)
street3.set_character(soldier)

street4 = lviv_game.Room("вулиця Козельницька")
street4.set_description("Final destionation and final boss")
Oles = lviv_game.Oles('Dobosevych','Dekan of APPS UCU', 9, 10000)
street4.set_character(Oles)


street1.link_room(street2, "south")
street2.link_room(street1, "north")
street2.link_room(street3, "west")
street3.link_room(street2, "east")
street3.link_room(street4, "south")
street4.link_room(street3, "north")


calculator = lviv_game.Item("calculator")
calculator.set_description("A calculator")
street1.set_item(calculator)


passport = lviv_game.Item("Passport")
passport.set_description("A passport")
street2.set_item(passport)

alkohol = lviv_game.Item("alkohol")
alkohol.set_description("An whiskey")
street3.set_item(alkohol)


current_room = street1
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            if inhabitant.name == 'Gopnik':
                abc = inhabitant.fight()
                if abc <= 0:
                    print('Gopnik killed u')
                    dead = True
                else:
                    print(f'You have {abc} lives more.')
                    current_room.character = None

            elif inhabitant.name == 'Soldier':
                years = 'a'
                while not years.isnumeric():
                    print('[Soldier]: Hello! How old are you!')
                    years = input('Your age: ')
                live = inhabitant.age(int(years))
                if live is True:
                    dead = True
                    break
                print('[Soldier]: Show me your passport!')
                if 'Passport' in backpack:
                    print('[Me]: Shows the pasport')
                    print('[Soldier]: Okay! you can go!')
                else:
                    print("You don't have a passport you lose")
                    dead = True
                current_room.character = None
            else:
                print('Final boss. A calculator will make your life simple')
                a = randint(0,200)
                b = randint(0, 200)
                if 'calculator' in backpack:
                    print(f'What is {a} + {b}')
                    res = input('> ')
                    if res.isnumeric():
                        if int(res) == a + b:
                            print('You won the game')
                        else: 
                            print('You lost the game')
                        dead = True
                else:
                    print(f'What is {a} * {b}')
                    res = input('> ')
                    if res.isnumeric():
                        inhabitant.quest(a,b, int(res))
                        dead = True
            # # Do I have this item?
            # if fight_with in backpack:

            #     if inhabitant.fight(fight_with) == True:
            #         # What happens if you win?
            #         print("Hooray, you won the fight!")
            #         current_room.character = None
            #         if inhabitant.get_defeated() == 2:
            #             print("Congratulations, you have vanquished the enemy horde!")
            #             dead = True
            #     else:
            #         # What happens if you lose?
            #         print("Oh dear, you lost the fight.")
            #         print("That's the end of the lviv_game")
            #         dead = True
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
            if item.name == 'alkohol':
                print('You told the soldier that u are under 18 and then you take an alcohol...')
                print('You lose')
                dead = True
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)