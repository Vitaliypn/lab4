"""Game"""

class Room:
    """room class"""
    def __init__(self, name):
        """Init func"""
        self.name = name
        self.description = ''
        self.links = []
        self.character = None
        self.item = None
        self.moves = {}

    def set_description(self, description):
        """Setting dexcriptionm"""
        self.description = description

    def link_room(self, other, way):
        """Linking rooms"""
        self.links.append(f'The {other.name} is {way}')
        self.moves[way] = other

    def set_character(self, char):
        """Character made"""
        self.character = char

    def set_item(self, item):
        """items"""
        self.item = item

    def get_details(self):
        """Detailing the room"""
        print(self.name)
        print('--------------------')
        print(self.description)
        print('\n'.join(self.links))

    def get_character(self):
        """getting character"""
        return self.character

    def get_item(self):
        """getting item"""
        return self.item

    def move(self, command):
        """Moves"""
        if command in self.moves:
            return self.moves[command]
        else:
            print('There is no such move')


class Enemy:
    """Enemy class"""
    def __init__(self, name, description, health, attack):
        """Init func"""
        self.name = name
        self.description = description
        self.weakness = ''
        self.conversation = ''
        self.health = health
        self.attack = attack


    def describe(self):
        """describing"""
        print(f'{self.name} is here!' + '\n' + self.description)


    def fight(self):
        """fighting"""
        while self.health > 0:
            self.health -= player.attack()
            player.change_of_health(-self.attack)
            print(f'Gopnik punch you! You left with {player.health} hp')
        return player.health

    def get_defeated(self):
        """If defeat"""
        player.plus1()
        return player.point

class Gopnik(Enemy):
    def __init__(self, name, description, health, attack):
        """Init func"""
        super().__init__(name , description, health, attack)

class Soldier(Enemy):
    def __init__(self, name, description, health, attack):
        """Init func"""
        super().__init__(name , description, health, attack)

    def age(self, age):
        if age >= 18:
            print('Game over, you go to war')
            player.health -= self.attack
            return True
        else:
            print('You can walk around')


class Oles(Enemy):
    def __init__(self, name, description, health, attack):
        """Init func"""
        super().__init__(name , description, health, attack)

    def quest(self, a, b, multiply):
        if a * b == multiply:
            print('You won the game')
        else:
            print('You lose')
            player.health -= self.attack
        return True


class Item:
    """item class"""
    def __init__(self, name):
        """init func"""
        self.name = name
        self.description = ''

    def set_description(self, desp):
        """descrip"""
        self.description = desp

    def describe(self):
        """describing"""
        print(f'The [{self.name}] is here - '+ self.description)

    def get_name(self):
        """Getting name"""
        return self.name

class Weapon(Item):
    def __init__(self, name ,power):
        """Init func"""
        super().__init__(name)
        self.power = power

    def attack(self):
        """Attack func"""
        return self.power

class Support(Item):
    def __init__(self, name, heal):
        """Init func"""
        super().__init__(name)
        self.heal = heal

    def attack(self):
        """Init func"""
        return player.change_of_health(self.heal)

class Player:
    def __init__(self):
        """Init func"""
        self.health = 10
        self.current_room = None
        self.inventory = []
        self.power = 5
        self.point = 0

    def change_of_health(self, power):
        """Change of health"""
        self.health += power

    def plus1(self):
        """If beat opponent"""
        self.point +=1

    def end(self):
        """end of the game func"""
        return self.health < 0 or self.point >= 3

    def attack(self):
        if len(self.inventory) != 0:
            pass
        return self.power

player = Player()