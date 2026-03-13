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

    return [health, attack, defense, speed]

print("Battle Simulator")

fighter1= create_fighter("Fighter 1")
fighter2= create_fighter("Fighter 2")

round_number = 1

while fighter1[0]>0 and fighter2[0]>0:
print("Round {round_number}")

if fighter1[3] >= fighter2[3]:
    first=fighter1
    second=fighter2
    first_name="fighter1"
    second_name="fighter2"
else:
    first=fighter2
    second=fighter1
    first_name="fighter2"
    first_name="fighter1"

damage= calculate_damage(first,second)
second[0]-= damage
print(f{first_name} attacks for {damage} damage.")
print(f{second_name} health: {max(first[0], 0)}")

if second[0] >0:
    damage= calculate_damage(second,first)
    first[0] -=damage
    print(f"{second_name} attacks for {damage} damage.")
    print(f"{first_name} health: {max(first[0], 0)}")

round_number +=1

print("Battles over")

if fighter1[0]>0:
    print("Fighter 1 wins!!!!")
else:
    print("fighter 2 wins!!!!")
