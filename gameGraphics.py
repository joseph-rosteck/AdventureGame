import pygame
import math
import time
import gamefunctions

pygame.init()

# Initalizes variables
screen_height = 600
screen_width = 800
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
player_gold = 0
player_hp = 30
player_inventory = {}
interaction_active = False
shop_visited = False
monster_fought = False



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
    hitbox = pygame.Rect(
    x - radius,  # Top left x
    y - radius,  # Top left y
    radius * 2, # Width
    radius * 2  # Height
    )
    return hitbox


# Creates screen 
screen = pygame.display.set_mode((screen_width, screen_height))
# Defines player size and where you spawn 
player = pygame.Rect(4,4,24,24) 
# How many pixels per movement
movement_amount = 32

clock = pygame.time.Clock()



running = True
while running:
##############################

    # Draws screen
    screen.fill((0,0,0))

    # Draws player
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Draws 10 by 10 white grid
    for row in range(10):
        for col in range(10):
            x = col * 32
            y = row * 32
            pygame.draw.rect(screen, white, (y, x, 32, 32), 1)

    # Draws test button
    #button1 = create_button(screen, 400, 10, 150, 50, white, "Inventory", black)
    #button2 = create_button(screen, 400, 70, 150, 50, white, "quit", black) 

    # Defines the total size of the grid
    grid_height = 320
    grid_width = 320

    # Draw the green shop circle
    shop_circle = create_circle(screen, 10, 1, 14, green)
    # Draw the red monster circle
    monster_circle = create_circle(screen, 10, 10, 14, red)

    
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
                                        

            #elif event.type == pygame.MOUSEBUTTONDOWN:
                #mouse_pos = pygame.mouse.get_pos()
                #if button1.collidepoint(mouse_pos):
                #    print("pressed inventory")
                #elif button2.collidepoint(mouse_pos):
                #    print("pressed quit")

    if not interaction_active:
        if player.colliderect(shop_circle) and not shop_visited:
            interaction_active = True  # Block inputs
            shop_visited = True  # Mark the shop as visited
            gamefunctions.print_shop_menu('Sword', 10.00, 'Fire Scroll', 20.00, player_gold)
            interaction_active = False  # Unlock inputs after interaction

        elif player.colliderect(monster_circle) and not monster_fought:
            interaction_active = True  # Block inputs
            monster_fought = True  # Mark the monster as fought
            fmreturn = gamefunctions.fight_monster(player_hp, player_gold, player_inventory)
            player_hp, player_gold = fmreturn
            interaction_active = False  # Unlock inputs after interaction

    # Reset flags when the player leaves the hitbox
    if not player.colliderect(shop_circle):
        shop_visited = False
    if not player.colliderect(monster_circle):
        monster_fought = False

##############################


    # Updates display
    pygame.display.update()

    # Sets framerate to 60
    clock.tick(60)

   

pygame.quit()
