import pygame
from gui import GUIManager, Dropdown

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Dropdown Example")
clock = pygame.time.Clock()
gui = GUIManager()

def on_select(option):
    print(f"Selected: {option}")

dropdown = Dropdown((100, 100, 200, 30), ["Apple", "Banana", "Cherry"], callback=on_select)
gui.add(dropdown)

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
