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
class Win:
    """win class"""
    def __init__(self):
        """aaa"""
        self.point = 0

    def plus1(self):
        """aaæ"""
        self.point +=1

class Enemy:
    """Enemy class"""
    def __init__(self, name, description):
        """Init func"""
        self.name = name
        self.description = description
        self.weakness = ''
        self.conversation = ''
        self.points = 0

    def set_conversation(self, phrase):
        """convesrsation func"""
        self.conversation = phrase

    def set_weakness(self, weak):
        """Weaknesses"""
        self.weakness = weak

    def describe(self):
        """describing"""
        print(f'{self.name} is here!' + '\n' + self.description)

    def talk(self):
        """Talking"""
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item):
        """fighting"""
        if item == self.weakness:
            print(f'You fend {self.name} off with the {item}')
        else:
            print(f'{self.name} crushes you, puny adventurer!')
        return item == self.weakness

    def get_defeated(self):
        """If defeat"""
        self.points += 1
        win.plus1()
        return win.point


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

win = Win()
    