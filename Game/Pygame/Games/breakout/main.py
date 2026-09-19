import pygame
import paddle

pygame.init()

# Global Variables
WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Player Variables
player_width = 70
player_height = 20

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50 - player_height // 2

player_speed = 5

player = paddle.Paddle(player_x, player_y, player_width, player_height, player_speed, CYAN, WIDTH)

# Ball Variables
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_speed_x = 3
ball_speed_y = 3

# Brick Variables
brick_width = 40
brick_height = 20
brick_color = ORANGE

brick_padding = 5

brick_top_offset = 50

brick_rows = 5
brick_cols = 15

brick_x_offset = (WIDTH - (brick_cols * (brick_width + brick_padding)) - brick_padding) // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + brick_x_offset
        brick_y = row * (brick_height + brick_padding) + brick_top_offset
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input Handling
    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    # Game Logic
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1

    player_rect = player.get_rect()
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

    if player_rect.colliderect(ball_rect):
        ball_speed_y *= -1
        ball_y = player.y - ball_radius  
        
    for brick in bricks:
        if brick.colliderect(ball_rect):
            ball_speed_y *= -1
            bricks.remove(brick)
            break

    # Game Over Logic
    if ball_y + ball_radius >= HEIGHT:
        running = False

    # Draw Phase
    screen.fill(BLACK)
    player.draw(screen)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)
    
    for brick in bricks:
        pygame.draw.rect(screen, brick_color, brick)

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()