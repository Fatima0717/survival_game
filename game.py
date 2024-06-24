import random
import time

def show:instructions():
print("""
      """)

def show_status():
    print('---------------------------')
    print(f'You are at the {current_area}')
    print(f'Helth: {health}')
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
        'Beach': "The beach is beautifull"
        'Jungle': "The jungle is dense"
        'cava': "The cave is dark"
        'Hill': "The hill provides"
        'River': "The river is flowing"
        'Clearing': "The clearing is open"
    }
    print(random.choice(events))

areas = {
    'Beach': {
        'north': 'jungle',
        'item': 'driftwood',
        'character': 'a friendly crab'
    },
    'Jungle': {
        'south': 'Beach',
        'east': 'Cava',
        'west': 'River',
        'item': 'fruit'
    },
    'Cava': {
        'west': 'jungle',
        'item': 'binoculars',
    },
    'Hill': {
        'east': 'Clearing',
        'item': 'binoculars',
    },
    'River': {
        'east': 'jungle',
        'item': 'fish',
    },
    'clearing': {
        'west': 'Hill',
        'item': 'signal flare',
    },
}

current_area = 'Beach'
inventory = []
health = 100
hunger = 0
thirst = 0

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

    command = move[]

    if command == 'go' and len(move) > 1:
        direction = move[1]
        if direction in areas[current_area]:
            current_area = areas[current_area][direction]
            random_events()
            hunger += 10
            thirst += 10
            health -= 5
        else:
            print("You can't go that way!")
    
    elif command == 'get' and len(move) > 1:
        item = move[1]
        if "item" in areas[current_area] and item == areas[current_area]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del areas[surrent_area]['item']
        else:
            print(f"can't get {item}!")
    
    elif command == 'look':
        print(describe_area(current_area))

    elif command == 'use' and len(move) > 1:
        item = move[1]
        if item == 'fruit':
            print("You get the fruit and feel refreshed! Yum!")
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
        elif item == 'flint'
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
    
    elif command