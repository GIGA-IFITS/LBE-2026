import pygame

# 1. INITIALIZATION
pygame.init()

# Setup Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Pertamaku - MandyTjandra")

# Setup Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Setup FPS (Frame Per Second regulator)
clock = pygame.time.Clock()

# --- PLAYER VARIABLES ---
# Write the variables position_x, position_y, size, and speed below:
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5
player_size = 50


# 2. GAME LOOP (Main program)
running = True
while running:
    # ---------------------------------------------
    # STAGE 1: EVENTS (Check User Input)
    # ---------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Exit the loop

    # Write logic to check keyboard arrow keys (K_LEFT, K_RIGHT, etc) here:
    keys = pygame.key.get_pressed()
    # TODO: Add player movement logic here
    
    
    # ---------------------------------------------
    # STAGE 2: UPDATE (Update Logic/Position)
    # ---------------------------------------------
    # TODO: Add screen boundary logic here for a challenge


    # ---------------------------------------------
    # STAGE 3: RENDER (Redraw)
    # ---------------------------------------------
    # Always clear the screen (like erasing a whiteboard)
    screen.fill(WHITE)

    # TODO: Draw player (blue box) to the screen using pygame.draw.rect()
    
    
    # Apply changes to the computer screen
    pygame.display.update()
    
    # Limit frame rate to 60 FPS
    clock.tick(60)

# 3. EXIT PYGAME
pygame.quit()
