import pygame
from gui import GUIManager, InputBox, Label

pygame.init()
screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("InputBox Example")
clock = pygame.time.Clock()
gui = GUIManager()

input_box = InputBox((150, 80, 200, 30))
label = Label((10, 80, 140, 30), "Enter Name:")
gui.add(label)
gui.add(input_box)

running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        gui.handle_event(event)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and input_box.active:
            print(f"Input: {input_box.text}")

    gui.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
