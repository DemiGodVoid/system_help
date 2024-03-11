import pygame
import sys
import psutil
import os

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

# Function to open tapps.py
def open_tapps():
    current_dir = os.path.dirname(__file__)
    tapps_path = os.path.join(current_dir, "tapps.py")
    if os.path.isfile(tapps_path):
        os.system('python "{}"'.format(tapps_path))
    else:
        print("Error: tapps.py not found in the same directory.")


# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Control Panel")

# Load font
font = pygame.font.Font(None, 30)

# Main loop
running = True
while running:
    screen.fill(BLACK)

    # Draw the "Hard Restart Browser" button
    button_rect1 = pygame.Rect(50, 100, 200, 50)
    pygame.draw.rect(screen, BLUE, button_rect1)
    
    # Render button text
    text_surface1 = font.render("Hard Restart Browser", True, BLACK)
    text_rect1 = text_surface1.get_rect(center=button_rect1.center)
    screen.blit(text_surface1, text_rect1)

    # Draw the "Terminate apps" button
    button_rect2 = pygame.Rect(350, 100, 200, 50)
    pygame.draw.rect(screen, BLUE, button_rect2)
    
    # Render button text
    text_surface2 = font.render("Terminate apps", True, BLACK)
    text_rect2 = text_surface2.get_rect(center=button_rect2.center)
    screen.blit(text_surface2, text_rect2)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect1.collidepoint(event.pos):
                force_close_browsers()  # Call the function to close browsers
            elif button_rect2.collidepoint(event.pos):
                open_tapps()  # Call the function to open tapps.py

    pygame.display.flip()

pygame.quit()
