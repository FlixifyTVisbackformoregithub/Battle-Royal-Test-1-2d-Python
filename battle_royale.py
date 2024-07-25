import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 30
GROUND_HEIGHT = 50
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Battle Royale")

# Player setup
player_rect = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - GROUND_HEIGHT - PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_rect.x += PLAYER_SPEED

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
    pygame.draw.rect(screen, (0, 0, 255), player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
