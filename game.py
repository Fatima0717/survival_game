import random
import time

def show:instructions():
print("""
      """)

def show_status():
    print('')
    print(f'You are at the {current_area}')
    print(f'Helth: {health}')
    print(f'Hunger: {hunger}')
    print(f'Thirst: {thirst}')
    print(f'Inventory: {inventory}')
    if "item" in areas[current_area]:
        print(f'You see a {areas}')
