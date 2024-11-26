import random

def show_instructions():
    print('---------------------------')
    print('Welcome to the Adventure Game!\n')
    print('Instructions:')
    print("1. Use 'go [direction]' to move (e.g., 'go north').")
    print("2. Use 'get [item]' to pick up an item.")
    print("3. Use 'look' to see a description of your current area.")
    print("4. Use 'use [item]' to utilize an item from your inventory.")
    print("5. Type 'inventory' to see the items you\'ve collected.")
    print("6. If health reaches 0, or hunger/thirst hits 100, the game ends.\n")
    print('Good luck!')
    print('---------------------------')

def show_status():
    print('---------------------------')
    print(f'You are at the {current_area}')
    print(f'Health: {health}')
    print(f'Hunger: {hunger}')
    print(f'Thirst: {thirst}')
    print(f'Inventory: {inventory}')
    if "item" in areas[current_area]:
        print(f'You see a {areas[current_area]["item"]}')
    if "character" in areas[current_area]:
        print(f'You see {areas[current_area]["character"]}')
    print('---------------------------')

def describe_area(area):
    descriptions = {
        'Beach': "The beach is beautiful with golden sands and gentle waves.",
        'Jungle': "The jungle is dense and full of mysterious sounds.",
        'Cave': "The cave is dark and echoes with strange noises.",
        'Hill': "The hill provides a breathtaking view of the surroundings.",
        'River': "The river is flowing swiftly, glistening under the sun.",
        'Clearing': "The clearing is open and serene, with sunlight streaming in.",
        'Jumping': "You feel a sense of weightlessness here, as if flying."
    }
    return descriptions.get(area, "Unknown area")

def random_events():
    if random.random() < 0.5:  # 50% chance of triggering an event
        events = [
            "You find a hidden path.",
            "A wild animal appears!",
            "You stumble upon a treasure chest.",
            "You feel a sudden drop in temperature.",
        ]
        print(random.choice(events))

areas = {
    'beach': {
        'north': 'jungle',
        'item': 'driftwood',
        'character': 'a friendly crab'
    },
    'jungle': {
        'south': 'Beach',
        'east': 'Cave',
        'west': 'River',
        'item': 'banana'
    },
    'cave': {
        'west': 'jungle',
        'item': 'binoculars',
    },
    'hill': {
        'east': 'Clearing',
        'item': 'golden sword',
    },
    'river': {
        'east': 'jungle',
        'item': 'fish',
    },
    'clearing': {
        'west': 'Hill',
        'item': 'signal flare',
    },
    'jumping': {
        'west': 'River',
        'item': 'Nintendo',
    }
}

current_area = 'Beach'
inventory = []
health = 100
hunger = 0
thirst = 0

show_instructions()

while True:
    show_status()

    if health <= 0 or hunger >= 100 or thirst >= 100:
        print("You didn't survive the island. Game over!")
        break

    move = input('>').lower().split()

    if len(move) == 0:
        print("Invalid command. Try again.")
        continue

    command = move[0]

    if command == 'go' and len(move) > 1:
        direction = move[1]
        if direction in areas[current_area]:
            current_area = areas[current_area][direction]
            random_events()
            hunger += 15
            thirst += 10
            health -= 5
        else:
            print("You can't go that way!")
    
    elif command == 'get' and len(move) > 1:
        item = move[1]
        if "item" in areas[current_area] and item == areas[current_area]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del areas[current_area]['item']
        else:
            print(f"Can't get {item}!")

    elif command == 'look':
        print(describe_area(current_area))

    elif command == 'use' and len(move) > 1:
        item = move[1]
        if item in inventory:
            if item == 'banana':
                print("You eat the banana and feel refreshed!")
                hunger = max(hunger - 20, 0)
                inventory.remove(item)
            elif item == 'fish':
                print("You cook the fish and have a hearty meal.")
                hunger = max(hunger - 30, 0)
                inventory.remove(item)
            elif item == 'driftwood':
                print("You use the driftwood to make a fire. It feels warm and safe.")
                thirst = max(thirst - 10, 0)
                health = min(health + 10, 100)
                inventory.remove(item)
            elif item == 'binoculars':
                print("You use the binoculars to scan the horizon.")
            elif item == 'signal flare':
                print("You use the signal flare to attract attention.")
                print("Congratulations! You survived the island!")
                break
            else:
                print(f"Using {item} doesn't seem to do anything useful.")
        else:
            print(f"You don't have a {item} in your inventory.")
    
    elif command == 'inventory':
        print(f"Inventory: {inventory}")

    else:
        print("Invalid command. Try again.")