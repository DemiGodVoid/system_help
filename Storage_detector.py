import pygame
import os
import psutil

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 400, 200
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FONT_SIZE = 20
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Junk Cleaner")

# Load font
font = pygame.font.SysFont(None, FONT_SIZE)

# Function to clear junk
def clear_junk():
    folder_path = get_screenshot_folder_path()
    if folder_path:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("Junk cleared successfully!")
    else:
        print("Screenshots folder not found.")

# Function to get local disk (C:) usage
def get_disk_usage():
    usage = psutil.disk_usage('/')
    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    return total_gb, used_gb

# Function to get screenshot folder path
def get_screenshot_folder_path():
    user_profile_path = os.path.expanduser("~")
    screenshot_folder_path = os.path.join(user_profile_path, "Pictures", "Screenshots")
    if os.path.exists(screenshot_folder_path):
        return screenshot_folder_path
    else:
        return None

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, True, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)

# Main loop
def main():
    running = True

    while running:
        screen.fill(WHITE)

        # Draw disk usage
        total_gb, used_gb = get_disk_usage()
        disk_usage_text = f"Disk Usage (C:): {used_gb:.2f} GB / {total_gb:.2f} GB"
        draw_text(disk_usage_text, font, BLUE, screen, 10, 10)

        # Draw button
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, 120, BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, BLUE, button_rect)
        draw_text("Clear Junk", font, WHITE, screen, WIDTH // 2, 145)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(mouse_pos):
                    clear_junk()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
