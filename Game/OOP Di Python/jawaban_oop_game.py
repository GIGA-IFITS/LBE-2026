import pygame
import random

# ==========================================
# OOP SECTION (OBJECT-ORIENTED PROGRAMMING)
# ==========================================

# 1. PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255)) 
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
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
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0)) # Red Color
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100) # Initial position
        
    def random_teleport(self):
        # Move the enemy to a random position inside the screen
        self.rect.x = random.randint(0, 800 - 50)
        self.rect.y = random.randint(0, 600 - 50)

# ==========================================
# PYGAME LOOP SECTION
# ==========================================

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Latihan OOP & Collision (Jawaban)")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
score = 0

player = Player()
enemy = Enemy()

running = True
while running:
    # 1. EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. UPDATE
    player.update()
    
    # Collision Detection
    if player.rect.colliderect(enemy.rect):
        score += 1
        enemy.random_teleport()

    # 3. RENDER
    screen.fill((255, 255, 255))
    
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
