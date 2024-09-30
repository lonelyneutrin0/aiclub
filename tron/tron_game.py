import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Tron Game")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))  # Black background

    # Draw a simple shape (a rectangle)
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 50, 30))  # Red rectangle

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()