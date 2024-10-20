import gamefunctions

name = input("What is your name?:")
print(gamefunctions.print_welcome(name))

item1name = input('What is the first item the shop is selling?:')
item1price = float(input('What is the price of the first item?:'))
item2name = input('What is the second item the shop is selling?:')
item2price = float(input('What is the price of the second item?:'))
print(gamefunctions.print_shop_menu(item1name, item1price, item2name, item2price))

itemPrice = float(input('What is the price of the item you want to buy?:'))
startingMoney = float(input('How much money do you have?:'))
quantityToPurchase = int(input('How many do you want to buy?:'))
print(gamefunctions.purchase_item(itemPrice, startingMoney, quantityToPurchase))

print(gamefunctions.new_random_monster())
