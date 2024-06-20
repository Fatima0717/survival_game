import random

def show_instructions():
    print("""
    Welcome to the Adventure Game!
    Your mission: Find the reasure hidden in one of the rooms. Beware of the unexpected!

    Commands:
      go [direction] - Move to another room (north, south, east, west)
      get [item] - Pick up an item
      look - Describe the current room
      use [item] - Use an item from your inventory
      quit - Exit the game 
    """)

def show_status():
    print('---------------------------')
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')
    print('---------------------------')

def describe_room(room):
    describe = {
        'Hall': "The hall is grand with a high celling and a large chandelier that makes you feel small. A talking portrait hangs on the wall.",
        'Kitchen': "The kitchen is messy with pots and pans everywhere. A chef ghost is cooking up some invisible stew.",
        'Dining Room': "The dining room has a large table set for a feast, but no one is around. A singing fish is mounted on the wall.",
        'Garden': "The garden is lush with flowers and a small pond. A gnome is fishing and whiseling a merry tune",
        'Library': "The library is quiet with walls lined with books. A floating bool is reading itself out loud.",
        'Basement': "The basement is dark and musty, filled with old furniture. A friendly spider waves at you "
    }
    return descriptions.get(room, "This place is indescribable. It's just too weird!")

# Define the game rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'north': 'Library',
        'west': 'Basement',
        'item': 'key'
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
        'north': 'Dining Room',
        'item': 'treasure'
    },
    'Library': {
        'south': 'Hall',
        'item': 'map'
    },
    'Basement': {
        'east': 'Hall',
        'item': 'flashlight'
    }

}

# Start the player in the Hall
current_room = 'Hall'
inventory = []

# Display instructions
show_instructions()

# Main game loop
while True:
    show_status()

    # Get the player's next move
    move = input('>').lower().split()

    if len(move) == 0:
        print("Invalid command. Try again.")
        continue

    command = move[0]

    if command == 'go' and len(move) > 1:
        direction = move[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            # Random events
            if random.choice([True, False]):
                event = random.choice([
                    "A mysterious wind blows through the room... Spookey!",
                    "You hear adistant laugh... Meow!",
                    "A ghost cat walks through the wall... Meow!",
                    "You find a piece of candy on the fooor.. Yum!"
                ])
                print(event)
        else:
            print("You can't go that way!")

    elif command == 'get' and len(move) > 1:
        item = move[1]
        if "item" in rooms[current_room] and item == rooms[current_room]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del rooms[current_room]['item']
        else:
            print(f"Can't get {item}!")

    elif command == 'look':
        print(describe_room(current_room))

    elif command == 'use' and len(move) > 1:
        item = move[1]
        if item in inventory:
        #Humorous responses for using items
             if item == 'potion':
                 print("You drink the potion and feel refreshed! Yum!")
                 inventory.remove(item)
             elif item == 'map':
                 print("You look at the map and get a better sense of the layout. very helpful")
             elif item == 'flashlight':
                 print(f"You turn on the flashlight and can see better sense of the layout. Much better!")
             else:
                 print(f"You can't use the {item} here.")
        else:
            print(f"You don't have a {item} in your inventory.")

    elif command == 'quit':
        print("Thanks for playing! come back soon!")
        break 

    else:
        print("Invalid command. Try again.")
       
    if 'treasure' in inventory:
        print("Congratulations! You found the treasure! You're rich!")
        break

    if 'monster' in inventory:
        print("A monster has caught you! Game over! Better luck next time")
        break
