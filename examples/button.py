import pygame
from gui import GUIManager, Button

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Button Example")
clock = pygame.time.Clock()
gui = GUIManager()

def on_click():
    print("Button clicked!")

gui.add(Button((100, 70, 200, 50), "Click Me", on_click))

running = True
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
