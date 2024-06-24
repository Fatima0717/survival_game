import random

def show_instructions():
    print("""
    welcome to Takuya room!
    your mission: find the tresure hidden in one iif the rooms. Beware of the unxpected!

    commands:
     go [direction] - move to another room
     get [item] - pick up an item
     look - 
     use [item]
     talk
     quit - Exit the game
    """)

def show_status():
    print('---------------------------')
    print(f'you are in the {current_room}')
    print(f'Inventory: {inventory})
    if "item" in rooms [current_room]:
          print(f'You see a {rooms[current_room]["item"]})
    if "character" in rooms[current_room]:
          print(f'You see {rooms[current_room]["character"]}')
    print('---------------------------')

def describe_room(room):
    descriptions = {
        'Hall': "Hall is shool hoall"
        'Kitchen': "New Kitchen"
        'Dinig Room': "Huge room"
        'Garden': "big"
        'Library': "small"
        'Basement': "undergrand"
    }
    return descriptions.get(room, "This place is indescribable. It's just too weird!")

rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dinig Room',
        'north': 'Library',
        'west': 'Basement',
        'item': 'key',
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion'
    },
    'Garden': {
        'north': 'Dininf Room',
        'item': 'treasure'
    },
    'Library': {
        'south': 'Hall',
        'item': 'map'
    },
    'Basement': {
        'east': 'Hall',
        'item': 'flashlight'
    },
    'Attic': {
        'down': 'Hall',
        'item': 'lamp'
    },
    'Bathroom': {
        'item': 'soap',
    },
    'Bedroom': {
        'item': 'lamp'
    },
    'Balcony': {
        'item': 'binoculars'
    }

}

current_room = 'Hall'
inventory = []

show_instructions()

while True:
    show_status()

    move = input('>').lower().split()

    if len(move) == 0:
        print("Invalid command. Try again.")
        continue

    command = move[0]

    if command == 'go' and len(move) > 1:
        direction = move[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]

            if random.choice([True, False]):
                event =random.choice([
                    "A mysterious Spooky!",
                    "You hear a distant",
                    "A gost"
                    "You find"
                ])
                print(event)
        else:
            print("You can't go that way!")

    elif command =='get' and len(move) > 1:
        item = move[1]
        if "item" in rooms[current_room] and item == rooms[current_room]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del rooms[current_room]['item']
        else:
            print(f"can't get {item}!")

    elif command == 'look':
        print(describe_room(current_room))

    elif command == 'use' and len(move) > 1:
        item = move[1]
        if item in inventory:
            if item == 'potion':
                print("You drink the potion")
                inventory.remove(item)
            elif item == 'map':
                print("You look at the map")
            elif item =='flashlight':
                print("You turn on the flashlight")
            else:
                print(f"You don't have a {item} in your inventory")
        else:
            print(f"You don't have a {item} in your inventory.")
    
    elif  command == 'talk' and len(move) > 1:
        character = move[1]
        if "character" in rooms[current_room] and character in rooms[current_room]['character']
            print(f'You talk to {rooms[current_room]["charaacter"]}.')
        else:
            print(f'There is no {character} here to talk to.')

    elif command == 'quit':
        print("Thank for playing! come back soon!")
        break
    else:
        print("Invalid command.Try again")
    
    if 'treasure' in inventory:
        print("Congratulation!")
        break

    if 'monstor' in inventory:
        print("A monster has caught you !")
        break
