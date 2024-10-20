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
    print(f'\'{message: ^20}\'')

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
    
    print(top_border)
    print(f'| {item1name: <12}{item1dollar: >8} |')
    print(f'| {item2name: <12}{item2dollar: >8} |')
    print(bottom_border)

####################################
print()
print()
####################################

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
print()
print()
####################################

def test_functions():
    print("purchase_item base test")
    print("item price = 1.23, starting money = 10, quantity purchased = 3")
    print(purchase_item(1.23, 10, 3),"\n")
    ###
    print("purchase_item default quantity test")
    print("item price = 3, starting money = 10")
    print(purchase_item(3,10),"\n")
    ###
    print("purchase_item too many items test")
    print("item price = 3, starting money = 10 quantity purchased = 29")
    print(purchase_item(3, 10, 29),"\n\n")
    ###
    print(new_random_monster(),"\n")
    print(new_random_monster(),"\n")
    print(new_random_monster(),"\n")

####################################

if __name__ == "__main__":
    test_functions()

    

    
