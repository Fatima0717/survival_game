import random

def show_instructions():
    print("""
    
          """)

def show_status():

def describe_room(room):
    descriptions = {

    }
    return descriptions.get(room,)

rooms = {
    'Hall': {
        'south': 'kitchen'
    }
    'Kitchen': {

    }
    'Dinig room':{
        'west':
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

    command = move

    if command == 'go' and len(move) > 1:
        direction = move[1]
        if direction in rooms[current_room]
            current_room = rooms[current_room][direction]

            if random.choice([True,False]):
                event = random.choice([

                ])
                print(event)
        else:
            print("You can't go that way!")
        
    elif command == 'get' and len(move) > 1:
        item = move[1]
        if "item" in rooms[current_room]and item == rooms[current_room]['item']:
            inventory.append(item)
            print(f'{item} got!')
            del rooms[current_room]['item']
        else:
            print(f"can't get {item}!")
    elif 