import pygame

# ==========================================
# OOP SECTION (OBJECT-ORIENTED PROGRAMMING)
# ==========================================

# 1. PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create character image/appearance (Blue Box 50x50)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255)) 
        
        # Hitbox (Collision area) and its position
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        
        # Speed
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.speed

# 2. ENEMY CLASS
# TODO: Create Enemy(pygame.sprite.Sprite) Class here. 
# Make the box Red and place it at position (100, 100)




# ==========================================
# PYGAME LOOP SECTION
# ==========================================

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Latihan OOP & Collision (Starter)")
clock = pygame.time.Clock()

# CREATING OBJECT (INSTANTIATION)
player = Player()
# TODO: Create one enemy object from the Enemy Class you made


running = True
while running:
    # 1. EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. UPDATE
    player.update()
    
    # TODO: Collision Logic (Use colliderect between player.rect and enemy.rect)
    

    # 3. RENDER
    screen.fill((255, 255, 255))
    
    screen.blit(player.image, player.rect)
    # TODO: Draw the enemy to the screen too
    

    pygame.display.update()
    clock.tick(60)

pygame.quit()
