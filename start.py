import os
import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("System Helper ~ By void")

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load settings icon and resize it
settings_icon_path = os.path.join(script_dir, 'settings.png')
if not os.path.exists(settings_icon_path):
    print("Error: 'settings.png' not found in the script's directory.")
    pygame.quit()
    sys.exit()

settings_icon = pygame.image.load(settings_icon_path)
settings_icon = pygame.transform.scale(settings_icon, (50, 50))  # Resize the icon

# Load font
font = pygame.font.Font(None, 36)

# Create a darker blue color for the navigation bar
nav_bar_color = (0, 0, 150)  # Darker blue color

# Create a blue button with text "Check Storage"
button_color = (0, 0, 255)  # Blue color
button_text = font.render("Check Storage", True, (255, 255, 255))  # White text

# Create a blue button with text "Helpful Tools"
helpful_tools_color = (0, 0, 255)  # Blue color
helpful_tools_text = font.render("Helpful Tools", True, (255, 255, 255))  # White text

# Set button positions and sizes
button_rect = button_text.get_rect()
button_rect.center = (screen_width // 2, screen_height // 2 - 50)  # Center of the screen

helpful_tools_rect = helpful_tools_text.get_rect()
helpful_tools_rect.center = (screen_width // 2, screen_height // 2 + 50)  # Below the first button

# Function to open Storage_detector.py
def open_storage_detector():
    storage_script = os.path.join(script_dir, 'Storage_detector.py')
    print("Attempting to open:", storage_script)  # Debug print
    if os.path.exists(storage_script):
        subprocess.Popen([sys.executable, storage_script])
    else:
        print("Error: 'Storage_detector.py' not found in the script's directory.")


# Function to open tools.py through the folder it's in
def open_tools():
    tools_folder = os.path.join(script_dir, 'tools')  # Construct the path to the "tools" folder
    tools_script = os.path.join(tools_folder, 'tools.py')  # Construct the path to tools.py
    if os.path.exists(tools_script):
        subprocess.Popen([sys.executable, tools_script])
    else:
        print("Error: 'tools.py' not found in the tools folder.")



# Function to open settings.py
def open_settings():
    settings_script = os.path.join(script_dir, 'settings.py')
    if os.path.exists(settings_script):
        subprocess.Popen([sys.executable, settings_script])
    else:
        print("Error: 'settings.py' not found in the script's directory.")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_rect.collidepoint(event.pos):
                    open_storage_detector()
                elif helpful_tools_rect.collidepoint(event.pos):
                    open_tools()
                elif event.pos[0] < 60 and event.pos[1] < 60:  # Check if settings icon is clicked
                    open_settings()

    # Fill the navigation bar with darker blue color
    pygame.draw.rect(screen, nav_bar_color, (0, 0, screen_width, 60))

    # Add text in the middle of the navigation bar
    text_surface = font.render("System Helper", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, 30))
    screen.blit(text_surface, text_rect)

    # Blit "Check Storage" button onto the screen
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_rect.topleft)

    # Blit "Helpful Tools" button onto the screen
    pygame.draw.rect(screen, helpful_tools_color, helpful_tools_rect)
    screen.blit(helpful_tools_text, helpful_tools_rect.topleft)

    # Blit settings icon onto the screen
    screen.blit(settings_icon, (10, 10))  # Top left corner of the screen

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
