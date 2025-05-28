import pygame
from gui import GUIManager, Button

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame Button Example")
clock = pygame.time.Clock()
running = True

# Initialize GUI manager
gui = GUIManager()

# Define a button callback function
def on_button_click():
    print("🎉 Button was clicked!")

# Create and add a button to the GUI
btn = Button((100, 100, 200, 50), "Click Me!", on_button_click)
gui.add(btn)

# Main loop
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        gui.handle_event(event)

    gui.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
