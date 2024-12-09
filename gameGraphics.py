import pygame
import gamefunctions
import random

pygame.init()

# Initalizes variables
screen_height = 600
screen_width = 800
grid_height = 320
grid_width = 320
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
player_gold = 50
player_hp = 30
player_inventory = {}
interaction_active = False
shop_visited = False
monster_fought = False
game_state = "PLAY" # Possible states are PLAY, INVENTORY, REST, SHOP, FIGHT
player_moves = 0 # Tracks player moves for monster movement 

monsters = [] # List for all active monsters

# Loads Player and Monster images
try:
    player_image = pygame.image.load("Player.png")
except FileNotFoundError:
    print("Player image failed to load.")
    player_image = None

try:
    monster_image = pygame.image.load("Monster.png")
except FileNotFoundError:
    print("Monster image failed to load.")
    monster_image = None



# Creates object for buttons
def create_button(screen,x, y, width, height, color, text, text_color):
    
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect)
    font = pygame.font.Font(None, 36)

    # Render the text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Put the text onto the button
    screen.blit(text_surface, text_rect)

    #returns for collison detection
    return button_rect

# Creates object for circles w/ hitbox
def create_circle(screen, xgrid , ygrid, radius, color):
    x = (32 * xgrid - 16)
    y = (32 * ygrid - 16)
    pygame.draw.circle(screen, color, (x, y), radius)
    return pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

class WanderingMonster:
    def __init__(self, grid_width, grid_height):
        self.x = random.randint(0, grid_width // 32 - 1) * 32 
        self.y = random.randint(0, grid_height // 32 - 1) * 32
        self.monster_data = gamefunctions.new_random_monster()

    def move(self, grid_width, grid_height):
        """Moves the monster in a random direction within grid bounds."""
        directions = [(0, -32), (0, 32), (-32, 0), (32,0)]
        dx, dy = random.choice(directions)
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < grid_width and 0 <= new_y < grid_height:
            self.x, self.y = new_x, new_y

    def collides_with_player(self, player_rect):
        """Checks if the monster collides with you."""
        return pygame.Rect(self.x, self.y, 32, 32).colliderect(player_rect)

# Creates screen 
screen = pygame.display.set_mode((screen_width, screen_height))
# Defines player size and where you spawn 
player = pygame.Rect(4,4,24,24)
# How many pixels per movement
movement_amount = 32

def draw_game():
    # Draws Screen
    screen.fill(black)
    # Draws Player
    if player_image:
        player_image_scaled = pygame.transform.scale(player_image, (32, 32))
        screen.blit(player_image_scaled, (player.x, player.y))
    else:
        pygame.draw.rect(screen, blue, player)


    # Draws 10 by 10 white grid
    for row in range(10):
        for col in range(10):
            x = col * 32
            y = row * 32
            pygame.draw.rect(screen, black, (y, x, 32, 32), 1)

    # Draw monsters
        for monster in monsters:
            if monster_image:
                monster_image_scaled = pygame.transform.scale(monster_image, (32, 32))
                screen.blit(monster_image_scaled, (monster.x, monster.y))
            else:
                create_circle(screen, monster.x // 32 + 1, monster.y // 32 + 1, 14, red)


    # TODO For inventory functions
    #item_nums = 1 
    #for item_name, item_details in player_inventory.items():
     #   description = item_details['description']
      #  item_type = item_details['itemtype']
      #  item_text = font.render(item_name, True, white)
     #   screen.blit(item_text, (50, 100 + item_name * 40))

clock = pygame.time.Clock()



running = True
while running:
##############################

    if game_state == "PLAY":
        draw_game()

        # Draws 10 by 10 white grid
        for row in range(10):
            for col in range(10):
                x = col * 32
                y = row * 32
                pygame.draw.rect(screen, white, (y, x, 32, 32), 1)

        # Draws test button
        button1 = create_button(screen, 400, 10, 150, 50, white, "Inventory", black)
        button2 = create_button(screen, 400, 70, 150, 50, white, "quit", black) 


        # Draw the green shop circle
        shop_circle = create_circle(screen, 10, 1, 14, green)
    # TODO make inventory gui function
    #if game_state == "INVENTORY":
        #game_inventory(player_inventory, player_gold, screen)

    
##############################

    # Checks every loop key presses
    for event in pygame.event.get():
         # Checks every loop for quit
        if event.type == pygame.QUIT:
            running = False

        # Only allows player input if not in interaction
        if not interaction_active:
        # Checks event fo movement key presses
            if event.type == pygame.KEYDOWN:
                # Copy the current location for testing
                new_x, new_y = player.x, player.y
                
                if event.key == pygame.K_UP and player.y - movement_amount >= 0:
                    new_y -= movement_amount
                elif event.key == pygame.K_DOWN and player.y + movement_amount + player.height <= grid_height:
                    new_y += movement_amount
                elif event.key == pygame.K_LEFT and player.x - movement_amount >= 0:
                    new_x -= movement_amount
                elif event.key == pygame.K_RIGHT and player.x + movement_amount + player.width <= grid_width:
                    new_x += movement_amount

                player.x, player.y = new_x, new_y
                player_moves += 1

                # Moves each monster if necessary
                if player_moves == 2:
                    for monster in monsters:
                        monster.move(grid_width, grid_height)
                    player_moves = 0
                                        

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    game_state = "INVENTORY"
                elif button2.collidepoint(mouse_pos):
                    print("pressed quit")

    if not interaction_active:
        if player.colliderect(shop_circle) and not shop_visited:
            interaction_active = True  # Block inputs
            shop_visited = True  # Mark the shop as visited
            gamefunctions.print_shop_menu('Sword', 10.00, 'Fire Scroll', 20.00, player_gold)
            interaction_active = False  # Unlock inputs after interaction

        

    # Reset flags when the player leaves the hitbox
    if not player.colliderect(shop_circle):
        shop_visited = False

    for monster in monsters[:]:
        if monster.collides_with_player(player):
            print(f'Encounter with {monster.monster_data['name']}!')
            player_hp, player_gold = gamefunctions.fight_monster(player_hp, player_gold, player_inventory)
            monsters.remove(monster)
            
    if not monsters:
        for _ in range(2):
            monsters.append(WanderingMonster(grid_width, grid_height))


    # Updates display
    pygame.display.update()

    # Sets framerate to 60
    clock.tick(60)

   

pygame.quit()
