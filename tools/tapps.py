import pygame
import psutil
import os

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 250
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Terminate apps")

# Set up fonts
font = pygame.font.Font(None, 24)

# Function to terminate all running apps except the current script
def terminate_all_apps():
    current_pid = os.getpid()
    for proc in psutil.process_iter():
        try:
            # Check if the process is not the current script
            if proc.pid != current_pid:
                proc.terminate()
        except Exception as e:
            print(f"Error terminating process {proc.pid}: {e}")

# Main loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if terminate_button_rect.collidepoint(event.pos):
                terminate_all_apps()

    # Count the number of running processes
    running_apps = len([p.name() for p in psutil.process_iter(['pid', 'name'])])

    # Clear the screen
    window.fill((255, 255, 255))

    # Render running apps text
    running_apps_text = font.render(f"Running Apps: {running_apps}", True, (0, 0, 0))
    running_apps_rect = running_apps_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    window.blit(running_apps_text, running_apps_rect)

    # Render terminate button
    terminate_button_text = font.render("Terminate all apps", True, (255, 255, 255))
    terminate_button_rect = terminate_button_text.get_rect(center=(WIDTH//2, HEIGHT//2))
    pygame.draw.rect(window, (0, 128, 0), terminate_button_rect)
    window.blit(terminate_button_text, terminate_button_rect.topleft)

    # Render disclaimer text
    disclaimer_text = font.render("This might only close a few apps, working on a fix", True, (255, 0, 0))
    disclaimer_rect = disclaimer_text.get_rect(center=(WIDTH//2, HEIGHT - 30))
    window.blit(disclaimer_text, disclaimer_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
