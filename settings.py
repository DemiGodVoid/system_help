import pygame
import webbrowser

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Settings")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Fonts
button_font = pygame.font.SysFont(None, 30)
small_text_font = pygame.font.SysFont(None, 20)

# Texts
button_text_1 = "Join our Discord!"
small_text_1 = "To see beta versions and more"
button_text_2 = "Update"
small_text_2 = "Tap here to see if a new version is out!"

# Buttons
button_rect_1 = pygame.Rect(50, 50, 300, 50)
button_rect_2 = pygame.Rect(50, 120, 300, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_rect_1.collidepoint(event.pos):
                    webbrowser.open("https://discord.gg/5hgNB42uPe")
                elif button_rect_2.collidepoint(event.pos):
                    webbrowser.open("https://github.com/DemiGodVoid/system_help")

    # Clear the screen
    screen.fill(BLACK)

    # Draw buttons
    pygame.draw.rect(screen, BLUE, button_rect_1)
    pygame.draw.rect(screen, BLUE, button_rect_2)

    # Draw button texts
    button_text_render_1 = button_font.render(button_text_1, True, WHITE)
    button_text_rect_1 = button_text_render_1.get_rect(center=button_rect_1.center)
    screen.blit(button_text_render_1, button_text_rect_1)

    button_text_render_2 = button_font.render(button_text_2, True, WHITE)
    button_text_rect_2 = button_text_render_2.get_rect(center=button_rect_2.center)
    screen.blit(button_text_render_2, button_text_rect_2)

    # Draw small texts
    small_text_render_1 = small_text_font.render(small_text_1, True, WHITE)
    small_text_rect_1 = small_text_render_1.get_rect(center=(screen_width // 2, 95))
    screen.blit(small_text_render_1, small_text_rect_1)

    small_text_render_2 = small_text_font.render(small_text_2, True, WHITE)
    small_text_rect_2 = small_text_render_2.get_rect(center=(screen_width // 2, 165))
    screen.blit(small_text_render_2, small_text_rect_2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
