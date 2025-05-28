import pygame
from gui import GUIManager, Slider

pygame.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Slider Example")
clock = pygame.time.Clock()
gui = GUIManager()

def on_slider(value):
    print(f"Slider Value: {value:.2f}")

slider = Slider((100, 80, 300, 20), 0, 100, 50, on_slider)
gui.add(slider)

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
