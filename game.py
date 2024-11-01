import gamefunctions
gf = gamefunctions

def inital_testing():
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



##########################################



global player_gold
player_hp = 30
player_gold = 0
player_inventory = {}

def main(player_hp, player_gold):
    while True:
        gf.display_menu(player_hp, player_gold)
        choice = input("Choose an option: ")

########################

        if choice == '1':
            player_hp, player_gold = gf.fight_monster(player_hp, player_gold, player_inventory)

########################

        elif choice == '2':
            if player_gold >= 5:
                player_gold -= 5; player_hp = min(player_hp + 10, 30)
                print("You feel rested. Your HP is restored.")
            else:
                print("Not enough gold to sleep!")

########################

        elif choice == '3':
            item_purchased = gf.print_shop_menu('Sword', 10 ,'Scroll of Instant Death', 100, player_gold)
            if 'Sword' in item_purchased:
                player_gold -= 10
                player_inventory.update(item_purchased) 
            elif 'Scroll of Instant Death' in item_purchased:
                player_gold -= 100
                player_inventory.update(item_purchased) 
            elif item_purchased == 'poor':
                print('Come back when you have some more gold.')
            elif item_purchased == 'bye':
                print('Thanks for coming adventurer!\n\n')

########################

        elif choice == '4':
            gf.display_inventory(player_inventory, player_gold)

########################

        elif choice == '5':
            print("Goodbye!"); break
        else:
            print("Invalid choice. Please select a displayed number.")

########################

main(player_hp, player_gold)
    
