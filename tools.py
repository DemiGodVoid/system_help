import pygame
import sys
import psutil

# Function to check if a process belongs to a browser
def is_browser_process(process):
    browsers = ['chrome', 'firefox', 'edge', 'opera']  # Add more browsers if needed
    for browser in browsers:
        if browser in process.name().lower():
            return True
    return False

# Function to force close browser processes
def force_close_browsers():
    for proc in psutil.process_iter():
        if is_browser_process(proc):
            proc.terminate()

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 200
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hard Restart Browser")

# Load font
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Draw the button
    button_rect = pygame.Rect(50, 50, 300, 100)
    pygame.draw.rect(screen, BLUE, button_rect)
    
    # Render button text
    text_surface = font.render("Hard Restart Browser", True, BLACK)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                force_close_browsers()  # Call the function to close browsers

    pygame.display.flip()

pygame.quit()
