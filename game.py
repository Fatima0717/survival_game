import random
import time

def show_instructions():
    print('---------------------------')
    print('Welcome to the Adventure Game!\n')
    print('Instructions:')
    print("1. Use 'go [direction]' to move (e.g., 'go north').")
    print("2. Use 'get [item]' to pick up an item.")
    print("3. Type 'inventory' to see the items you\'ve collected.")
    print('\nGood luck!')
    print('---------------------------')

def show_status():
    print('---------------------------')
    print(f'You are at the {current_area}')
    print(f'Health: {health}')
    print(f'Hunger: {hunger}')
    print(f'Thirst: {thirst}')
    print(f'Exercise: {workout}')
    print(f'Inventory: {inventory}')
    if "item" in areas[current_area]:
        print(f'You see a {areas[current_area]["item"]}')
    if "character" in areas[current_area]:
        print(f'You see {areas[current_area]["character"]}')
    print('---------------------------')

def describe_area(area):
    descriptions = {
        'Beach': "The beach is beautiful",
        'Jungle': "The jungle is a mystery",
        'Cave': "The cave is dark and blue",
        'Hill': "The hill provides",
        'River': "The river is flowing",
        'Clearing': "The clearing is open",
        'Jumping': "He is flying"
    }
    print(descriptions.get(area,"Unknown area"))

def random_events():
    events = [
        "You find a hidden path.",
        "A wild animal appears!",
        "You stumble upon a treasure chest.",
        "You feel a sudden drop in temperature.",
    ]
    print(random.choice(events))

areas = {
    'Beach': {
        'north': 'jungle',
        'item': 'driftwood',
        'character': 'a friendly crab'
    },
    'Jungle': {
        'south': 'Beach',
        'east': 'Cave',
        'west': 'River',
        'item': 'Banana'
    },
    'Cave': {
        'west': 'jungle',
        'item': 'binoculars',
    },
    'Hill': {
        'east': 'Clearing',
        'item': 'Golden Sword',
    },
    'River': {
        'east': 'jungle',
        'item': 'fish and chips',
    },
    'Clearing': {
        'west': 'Hill',
        'item': 'Signal flare',
    },
    'Jumping': {
        'west': 'River',
        'item': 'Nintendo',
    }
}

current_area = 'Beach'
inventory = []
health = 100
hunger = 0
thirst = 0
workout =0

show_instructions()

while True:
    show_status()

    if health <=0 or hunger >= 100 or thirst >= 100:
        print("You didn't survive the island. Game over!")
        break

    move = input('>').lower().split()

    if len(move) ==0:
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
            workout -= 5
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
        if item == 'fruit':
            print("You get the fruit and feel refreshed!")
            hunger = max(huger - 20, 0)
            inventory.remove(item)
        elif item == 'fish':
            print("You use the driftwood to make a fire")
            hunger = max(hunger - 30, 0 )
            inventory.remove(item)
        elif item == 'driftwood':
            print("You use the driftwood to make a fire. it feels warm and safe.")
            thirst = max(thirst - 10,0 )
            health = min(health + 10, 100)
            inventory.remove(item)
        elif item == 'flint':
            print("You use the to start a fire")
            health = min(health + 10, 100)
            inventory.remove(item)
        elif item == 'binoculars':
            print("You use the binoculars to scan the horizon")
        elif item == 'signal flare':
            print("You use binoculars to scan the horizon for rescue.")
            print("Congratulations! You survived the island!")
            break
        else:
            print(f"You don't have a {item} in your inventory.")
    
    else:
        print("Invalid command. Try again.")