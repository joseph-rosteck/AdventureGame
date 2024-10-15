def print_welcome(name):
    '''Takes name and outputs Hello, "name"! centered in a 20 space field'''
    
    message = f'Hello, {name}!'
    print(f'\'{message: ^20}\'')

####################################

def print_shop_menu(item1name, item1price, item2name, item2price):
    '''Takes two items and two prices and puts them into a nice little shop menu'''
    
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

#####################################
print()
print()
#####################################

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

    

    
