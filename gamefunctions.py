"""
Module: Shop and Monster Simulation

This module contains functions for a simple shop interface and a random monster generator for a text-based game.

Functions:

1. print_welcome(name):
   Takes a player's name and prints a welcome message centered in a 20-space field.
   
   Parameters:
   - name (str): The name of the player.

2. print_shop_menu(item1name, item1price, item2name, item2price):
   Takes two item names and their corresponding prices and prints a formatted shop menu.
   
   Parameters:
   - item1name (str): The name of the first item.
   - item1price (float): The price of the first item.
   - item2name (str): The name of the second item.
   - item2price (float): The price of the second item.

3. purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
   Simulates purchasing items from the shop, returning the number of items purchased 
   and the leftover money.
   
   Parameters:
   - itemPrice (float): The price of the item.
   - startingMoney (float): The amount of money available to spend.
   - quantityToPurchase (int, optional): The desired quantity of items to purchase (default is 1).
   
   Returns:
   - tuple: A tuple containing the number of items purchased and the remaining money.

4. new_random_monster():
   Generates a random monster with associated attributes including name, description, 
   health, power, and money rewards.
   
   Returns:
   - dict: A dictionary containing the monster's name, description, health, power, 
     and the amount of money it can drop.

5. display_menu():
   Displays a menu with some options for and encounter or to rest.

   Parameters:
   - player_hp (int): Displays current hp for the player.
   - player_gold (int): Displays current gold for the player.

   Returns:
   - str: A few menu options so that you can you player input to do the thinghs on the menu.

6. fight_monster():
   Starts a loop for fights randomized monsters from new_random_monster().

   Parameters:
   - player_hp (int): Tracks current hp during encounters.
   - player_gold (int): Tracks current gold spent and gained during encounters.

   Returns:
   - str, int: Most everything is just interactive menus and integers are for health and gold.

Usage:
- The module is designed for a simple shop and monster encounter simulation in a text-based game.
- It includes example usage that demonstrates the functionality of the provided functions.

Example:
    print_welcome('Alice')
    print_shop_menu('Sword', 19.99, 'Shield', 12.50)
    purchases, remaining = purchase_item(5.00, 20.00, 5)
    monster = new_random_monster()
"""



def print_welcome(name):
    '''Takes name and outputs Hello, "name"! centered in a 20 space field.

    Parameters:
   - name (str): The name of the player.'''
    
    message = f'Hello, {name}!'
    return (f'\'{message: ^20}\'')

####################################

def print_shop_menu(item1name, item1price, item2name, item2price):
    '''Takes two items and two prices and puts them into a nice little shop menu.

    Parameters:
   - item1name (str): The name of the first item.
   - item1price (float): The price of the first item.
   - item2name (str): The name of the second item.
   - item2price (float): The price of the second item.'''
    
    top_border = '/' + ('-' * 22) + '\\' 
    bottom_border = '\\' + ('-' * 22) + '/'
    #creates the top and bottom border variables
    
    item1dollar = f'${item1price:.2f}'
    item2dollar = f'${item2price:.2f}'
    #converts the input float into a float with dollar signs and two digits after the decimal
    
    return (
        f'{top_border}\n' +  # Top border on its own line
        f'| {item1name: <12}{item1dollar: >8} |\n' +  # Item 1 with its price
        f'| {item2name: <12}{item2dollar: >8} |\n' +  # Item 2 with its price
        f'{bottom_border}'  # Bottom border on its own line
    )

####################################
def shop_and_names_test():
    print("print_welcome tests with names Bob, Ashley, and Bartholomew")
    print_welcome('Bob')
    print_welcome('Ashley')
    print_welcome('Bartholomew')
    print()
    print("print_shop_menu tests with Pear, 1.56, Bucket, 5.2")
    print_shop_menu("Pear",1.56,"Bucket",5.20)
    print()
    print("print_shop_menu tests with Broadsword, 20, Apple, 5.21111")
    print_shop_menu("Broadsword",20,"Apple",5.21111)
    print()
    print("print_shop_menu tests with Donkey, 109.99, Orange, 6")
    print_shop_menu("Donkey",109.99,"Orange",6)

####################################

import random
import time

####################################

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    '''Simulates purchasing items from the shop, returning the number of items purchased 
   and the leftover money.

   Parameters:
   - itemPrice (float): The price of the item.
   - startingMoney (float): The amount of money available to spend.
   - quantityToPurchase (int, optional): The desired quantity of items to purchase (default is 1).
   
   Returns:
   - tuple: A tuple containing the number of items purchased and the remaining money.'''
    
    while True: #loop so if quantityToPurchase is too high 
        if quantityToPurchase <= startingMoney // itemPrice:
            num_purchases = quantityToPurchase
            break
        else:
            quantityToPurchase = quantityToPurchase - 1
            continue
    
    leftover_money = startingMoney - (itemPrice * num_purchases)
    return num_purchases, leftover_money
    
###################################

def new_random_monster():
    '''Generates a random monster with associated attributes including name, description, 
   health, power, and money rewards.
   
   Returns:
   - dict: A dictionary containing the monster's name, description, health, power, 
     and the amount of money it can drop.'''
    
    names = ['Goblin', 'Troll', 'Dragon']
    
    descriptions = {
    "Goblin": "This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn.",
    "Troll": "A massive troll lumbers into your path, when it sees you it lets out a deafening roar.",
    "Dragon": "You spot the majestic dragon curled on top of its horde. When you cross the threshold of the cave, its eyes snap open.",
    }
    
    health_ranges = {
    "Goblin": (3, 10),
    "Troll": (15, 50),
    "Dragon": (100, 300),
    }
    power_ranges = {
    "Goblin": (1, 5),
    "Troll": (10, 25),
    "Dragon": (50, 100),
    }
    money_range = {
    "Goblin": (5, 10),
    "Troll": (25, 50),
    "Dragon": (100, 500),
    }

    name = random.choice(names)
    description = descriptions[name]
    health = random.randint(*health_ranges[name])
    power = random.randint(*power_ranges[name])
    money = random.randint(*money_range[name])
    
                  
    return {
        "name": name,
        "description": description,
        "health": health,
        "power": power,
        "money": money,
        }
        
####################################





####################################

def display_menu(player_hp, player_gold):
    """Displays the main game menu."""
    print(f"Current HP: {player_hp}, Current Gold: {player_gold}")
    print("What would you like to do?")
    print("1) Fight Monster")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Quit")

####################################

def fight_monster(player_hp, player_gold):
    """
    Logic for choosing and fighting monsters.

    Parameters:
        player_hp (int): The player's current health points.
        player_gold (int): The player's current gold amount.

    Returns:
        tuple: Updated player_hp and player_gold after the fight.
    """
     
     # Generate random monster stats
    monster_stats = new_random_monster()
    monster_hp = monster_stats["health"]
    monster_min_power = monster_stats["power"] // 2
    monster_max_power = monster_stats["power"]
    print(f'\nYou stumbled upon a {monster_stats["name"]}! Its power is {monster_stats["power"]}')
    
     # Loop until either the player or the monster is defeate
    while player_hp > 0 and monster_hp > 0:
        print(f'\nMonster Hp: {monster_hp}   Player Hp: {player_hp}\n')
        action = input('1) Attack!\n2) Run away.\n3) Quit\n')
        
         # Calculate damage dealt to monster and player
        if action == '1':
            damage_to_monster = random.randint(3, 10)
            damage_to_player = random.randint(monster_min_power, monster_max_power)

             # Update health points based on damage
            monster_hp -= damage_to_monster
            player_hp -= damage_to_player
            print(f"You dealt {damage_to_monster} damage to the monster.")
            print(f"The monster dealt {damage_to_player} damage to you.")

             # Checks for and edge case where both player and monster are defeated at the same time.
            if (monster_hp and player_hp) <= 0:
                print("You have been defeated by the monster!\n")
                time.sleep(1)
                exit() 
            if monster_hp <= 0:
                print(f'\nYou defeated the monster and got {monster_stats["money"]} gold!\n')
                player_gold += monster_stats["money"]
                break
            elif player_hp <= 0:
                print("You have been defeated by the monster!\n")
                time.sleep(1)
                exit() 
        elif action == '2':
            print("You ran away!\n")
            time.sleep(1)
            break
        elif action == '3':
            print("Exiting the game.\n")
            time.sleep(1)
            break
        else:
            print('Please choose 1, 2, or 3.')

     # Return updated health and gold after the fight
    return player_hp, player_gold



####################################







