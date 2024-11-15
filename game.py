import gamefunctions
import json
import time
gf = gamefunctions
#test

##########################################

global player_gold
player_hp = 30
player_gold = 0
player_inventory = {}

def main(player_hp, player_gold, player_inventory):
    while True:
        start_choice = input('Choose an option:\n1) New Game\n2) Load Game\n3) Quit\n')

        # Starts a new game.
        if start_choice == '1':
            break
        
        # Loads a saved game from a json file.
        elif start_choice == '2':
            filename = input('What is the name of your save?:\n')
            if '.json' not in filename: # Adds .json to file name if user doesn't add it.
                filename = filename + '.json'
            try:
                with open(filename, 'r') as file:
                    gamestate = json.load(file)
                    print('Game Loaded Successfuly!')
                    time.sleep(.5)
                    player_hp = gamestate['Health']
                    player_gold = gamestate['Gold']
                    player_inventory = gamestate['Inventory']
                    break
            except FileNotFoundError:
                print("Save file not found.")
                return None
            # Quits the game.
        elif start_choice == '3':
            print('Thanks for playing!')
            quit()


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
            if ('Sword' in item_purchased) and ('Sword' in player_inventory):
                print('Sorry you already have one of those!')
                time.sleep(.3)

            elif ('Scroll of Instant Death' in item_purchased) and ('Scroll of Instant Death' in player_inventory):
                print('Sorry you already have one of those!')
                time.sleep(.3)

            elif 'Sword' in item_purchased:
                player_gold -= 10
                player_inventory.update(item_purchased) 
                print('Thank you for your purchase!\n')
            elif 'Scroll of Instant Death' in item_purchased:
                player_gold -= 100
                player_inventory.update(item_purchased) 
                print('Thank you for your purchase!\n')

            elif item_purchased == 'poor':
                print('Come back when you have some more gold.')

            elif item_purchased == 'bye':
                print('Thanks for coming adventurer!\n\n')

########################

        elif choice == '4':
            gf.display_inventory(player_inventory, player_gold)

########################

        elif choice == '5':
            gamestate = {
                'Health': player_hp,
                'Gold': player_gold,
                'Inventory': player_inventory
            }
            filename = input('Please enter a name for your save:\n')
            if '.json' not in filename:
                filename = filename + '.json'
            with open(filename, 'w') as file:
                json.dump(gamestate, file, indent=4)
                print('Game saved successfuly!\n')
                time.sleep(.5)
            

        elif choice == '6':
            print("Goodbye!"); break
        else:
            print("Invalid choice. Please select a displayed number.")

########################

main(player_hp, player_gold, player_inventory)
    
