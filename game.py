def show_instructions():
    print("""
    Welcome to the Adventure Game!
    Find the treasure hidden in one of the rooms.

    Commands:
      go [direction]
      get [item]
      quit
    """)

def show_status():
    print('---------------------------')
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')
    print('---------------------------')

# Define the game rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
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

    if move[0] == 'go':
        direction = move[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    elif move[0] == 'get':
        item = move[1]
        if "item" in rooms[current_room] and item == rooms[current_room]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del rooms[current_room]['item']
        else:
            print(f"Can't get {item}!")

    elif move[0] == 'quit':
        print("Thanks for playing!")
        break

    if 'treasure' in inventory:
        print("Congratulations! You found the treasure!")
        break

    if 'monster' in inventory:
        print("A monster has caught you! Game over!")
        break
