import pygame
import random
import sys

# --- Initialization & Constants ---
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Micro-Monopoly")
FONT = pygame.font.SysFont("Arial", 18)
BIG_FONT = pygame.font.SysFont("Arial", 24, bold=True)
FPS = 30

# Colors
WHITE, BLACK, GRAY = (255, 255, 255), (0, 0, 0), (200, 200, 200)
RED, BLUE, GREEN, YELLOW = (255, 50, 50), (50, 50, 255), (50, 200, 50), (220, 220, 50)

# --- Classes ---
class Tile:
    def __init__(self, name, price=0, rent=0, type="property"):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
        self.type = type # "property", "go", "jail", "freeparking"

class Player:
    def __init__(self, name, color, is_ai=False):
        self.name = name
        self.color = color
        self.is_ai = is_ai
        self.money = 1500
        self.position = 0
        self.in_game = True

# --- Board Setup (20 tiles for simplicity: 5 per side) ---
board = [
    Tile("GO", type="go"),
    Tile("Med. Ave", 60, 2), Tile("Baltic Ave", 60, 4), Tile("Income Tax", type="tax"), Tile("Reading RR", 200, 25),
    Tile("JAIL", type="jail"),
    Tile("Oriental Ave", 100, 6), Tile("Vermont Ave", 100, 6), Tile("Conn. Ave", 120, 8), Tile("St. Charles", 140, 10),
    Tile("FREE PARKING", type="freeparking"),
    Tile("States Ave", 140, 10), Tile("Virginia Ave", 160, 12), Tile("Penn RR", 200, 25), Tile("St. James", 180, 14),
    Tile("GO TO JAIL", type="jail"),
    Tile("Tenn. Ave", 180, 14), Tile("NY Ave", 200, 16), Tile("Kentucky Ave", 220, 18), Tile("Indiana Ave", 220, 18)
]

# --- Game State ---
players = [
    Player("P1 (Human)", RED, is_ai=False),
    Player("P2 (AI)", BLUE, is_ai=True),
    Player("P3 (AI)", GREEN, is_ai=True),
    Player("P4 (AI)", YELLOW, is_ai=True)
]
current_player_idx = 0
state = "ROLL"  # States: ROLL, BUY_DECISION, GAME_OVER
message_log = ["Welcome to Micro-Monopoly!"]

def log_msg(msg):
    message_log.append(msg)
    if len(message_log) > 12:
        message_log.pop(0)

# --- Drawing Functions ---
def get_tile_rect(index):
    # Calculate x, y for a 20-tile board (5 per side)
    side_length = 5
    tile_w, tile_h = 80, 80
    offset_x, offset_y = 50, 50
    
    if 0 <= index < 5:    # Bottom edge (moving left)
        return pygame.Rect(offset_x + (5 - index) * tile_w, offset_y + 5 * tile_h, tile_w, tile_h)
    elif 5 <= index < 10: # Left edge (moving up)
        return pygame.Rect(offset_x, offset_y + (10 - index) * tile_h, tile_w, tile_h)
    elif 10 <= index < 15: # Top edge (moving right)
        return pygame.Rect(offset_x + (index - 10) * tile_w, offset_y, tile_w, tile_h)
    else:                  # Right edge (moving down)
        return pygame.Rect(offset_x + 5 * tile_w, offset_y + (index - 15) * tile_h, tile_w, tile_h)

def draw_board(surface):
    surface.fill(WHITE)
    for i, tile in enumerate(board):
        rect = get_tile_rect(i)
        
        # Color tile if owned
        bg_color = tile.owner.color if tile.owner else GRAY
        if tile.type != "property": bg_color = WHITE
        
        pygame.draw.rect(surface, bg_color, rect)
        pygame.draw.rect(surface, BLACK, rect, 2)
        
        # Text
        words = tile.name.split()
        for j, word in enumerate(words):
            text = FONT.render(word, True, BLACK)
            surface.blit(text, (rect.x + 5, rect.y + 5 + j*15))
        if tile.type == "property":
            price_text = FONT.render(f"${tile.price}", True, BLACK)
            surface.blit(price_text, (rect.x + 5, rect.y + rect.height - 20))

def draw_players(surface):
    for i, p in enumerate(players):
        if not p.in_game: continue
        rect = get_tile_rect(p.position)
        # Offset players so they don't overlap entirely
        px = rect.x + 10 + (i % 2) * 30
        py = rect.y + 10 + (i // 2) * 30
        pygame.draw.circle(surface, p.color, (px, py), 12)
        pygame.draw.circle(surface, BLACK, (px, py), 12, 1)

def draw_ui(surface):
    # Sidebar
    sidebar_x = 550
    pygame.draw.rect(surface, GRAY, (sidebar_x, 0, WIDTH - sidebar_x, HEIGHT))
    pygame.draw.rect(surface, BLACK, (sidebar_x, 0, WIDTH - sidebar_x, HEIGHT), 3)
    
    # Leaderboard
    y = 20
    surface.blit(BIG_FONT.render("PLAYERS:", True, BLACK), (sidebar_x + 10, y))
    y += 30
    for p in players:
        status = f"${p.money}" if p.in_game else "BANKRUPT"
        text = FONT.render(f"{p.name}: {status}", True, p.color)
        surface.blit(text, (sidebar_x + 10, y))
        y += 25
        
    # Controls / State
    y += 20
    surface.blit(BIG_FONT.render("CONTROLS:", True, BLACK), (sidebar_x + 10, y))
    y += 30
    if state == "ROLL":
        surface.blit(FONT.render("[SPACE] to Roll Dice", True, BLACK), (sidebar_x + 10, y))
    elif state == "BUY_DECISION":
        surface.blit(FONT.render("[B] to Buy, [P] to Pass", True, BLACK), (sidebar_x + 10, y))
        
    # Logs
    y += 50
    surface.blit(BIG_FONT.render("ACTIVITY LOG:", True, BLACK), (sidebar_x + 10, y))
    y += 30
    for msg in message_log:
        surface.blit(FONT.render(msg, True, BLACK), (sidebar_x + 10, y))
        y += 20

# --- Main Game Loop ---
clock = pygame.time.Clock()
ai_timer = 0

while True:
    current_player = players[current_player_idx]
    
    # Skip bankrupt players
    if not current_player.in_game:
        current_player_idx = (current_player_idx + 1) % len(players)
        continue

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if not current_player.is_ai:
            if event.type == pygame.KEYDOWN:
                if state == "ROLL" and event.key == pygame.K_SPACE:
                    # Roll Dice
                    roll = random.randint(1, 6) + random.randint(1, 6)
                    log_msg(f"{current_player.name} rolled a {roll}.")
                    current_player.position = (current_player.position + roll) % len(board)
                    
                    # Pass GO
                    if current_player.position < roll:
                        current_player.money += 200
                        log_msg(f"{current_player.name} passed GO! (+$200)")
                        
                    tile = board[current_player.position]
                    log_msg(f"{current_player.name} landed on {tile.name}.")
                    
                    # Resolve Tile
                    if tile.type == "property" and tile.owner is None:
                        state = "BUY_DECISION"
                    elif tile.type == "property" and tile.owner and tile.owner != current_player:
                        log_msg(f"{current_player.name} pays ${tile.rent} to {tile.owner.name}.")
                        current_player.money -= tile.rent
                        tile.owner.money += tile.rent
                        current_player_idx = (current_player_idx + 1) % len(players)
                    elif tile.type == "tax":
                        log_msg(f"{current_player.name} paid $50 tax.")
                        current_player.money -= 50
                        current_player_idx = (current_player_idx + 1) % len(players)
                    else:
                        current_player_idx = (current_player_idx + 1) % len(players)
                        
                elif state == "BUY_DECISION":
                    tile = board[current_player.position]
                    if event.key == pygame.K_b and current_player.money >= tile.price:
                        current_player.money -= tile.price
                        tile.owner = current_player
                        log_msg(f"{current_player.name} bought {tile.name}!")
                        state = "ROLL"
                        current_player_idx = (current_player_idx + 1) % len(players)
                    elif event.key == pygame.K_p:
                        log_msg(f"{current_player.name} passed on {tile.name}.")
                        state = "ROLL"
                        current_player_idx = (current_player_idx + 1) % len(players)

    # --- AI Logic ---
    if current_player.is_ai:
        ai_timer += 1
        if ai_timer > 30: # Delay for readability
            ai_timer = 0
            if state == "ROLL":
                roll = random.randint(1, 6) + random.randint(1, 6)
                log_msg(f"{current_player.name} rolled a {roll}.")
                current_player.position = (current_player.position + roll) % len(board)
                
                if current_player.position < roll:
                    current_player.money += 200
                    
                tile = board[current_player.position]
                log_msg(f"{current_player.name} landed on {tile.name}.")
                
                if tile.type == "property" and tile.owner is None:
                    state = "BUY_DECISION"
                elif tile.type == "property" and tile.owner and tile.owner != current_player:
                    log_msg(f"{current_player.name} pays ${tile.rent} to {tile.owner.name}.")
                    current_player.money -= tile.rent
                    tile.owner.money += tile.rent
                    current_player_idx = (current_player_idx + 1) % len(players)
                elif tile.type == "tax":
                    current_player.money -= 50
                    current_player_idx = (current_player_idx + 1) % len(players)
                else:
                    current_player_idx = (current_player_idx + 1) % len(players)
                    
            elif state == "BUY_DECISION":
                tile = board[current_player.position]
                # Simple AI: Always buy if it has enough money
                if current_player.money >= tile.price + 100: 
                    current_player.money -= tile.price
                    tile.owner = current_player
                    log_msg(f"{current_player.name} bought {tile.name}!")
                else:
                    log_msg(f"{current_player.name} passed on {tile.name}.")
                state = "ROLL"
                current_player_idx = (current_player_idx + 1) % len(players)

    # --- Bankruptcy Check ---
    for p in players:
        if p.money < 0 and p.in_game:
            p.in_game = False
            log_msg(f"{p.name} went BANKRUPT!")
            # Return properties to bank
            for t in board:
                if t.owner == p: t.owner = None

    # --- Drawing ---
    draw_board(SCREEN)
    draw_players(SCREEN)
    draw_ui(SCREEN)
    
    pygame.display.flip()
    clock.tick(FPS)