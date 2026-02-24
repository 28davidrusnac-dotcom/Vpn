import random

def calculate_damage(attacker, defender):
    base_damage = attacker[1] - defender[2]  # attack - defense
    
    if base_damage < 1:
        base_damage = 1

    # 20% chance of critical hit
    crit_roll = random.randint(1, 5)
    if crit_roll == 1:
        print("Critical hit!")
        base_damage *= 2

    return base_damage

def create_fighter(name):
    health= int(input(f"Enter {name}'s health: "))
    attack = int(input(f"Enter {name}'s attack power: "))
    defense = int(input(f"Enter {name}'s defense: "))
    speed = int(input(f"Enter {name}'s speed: "))

    return [health,attack, defense, speed]

print("Battle Simulator")