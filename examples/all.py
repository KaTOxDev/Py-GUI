import pygame
from gui import GUIManager, Button, InputBox, Label, Slider, CheckBox, Dropdown

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("All Widgets Example")
clock = pygame.time.Clock()
gui = GUIManager()

# === Input ===
name_input = InputBox((160, 20, 200, 30))
gui.add(Label((20, 20, 130, 30), "Enter Your Name:"))
gui.add(name_input)

# === Button ===
def on_button_click():
    print(f"Button clicked! Name input: {name_input.text}")
gui.add(Button((400, 20, 150, 30), "Submit", on_button_click))

# === Slider ===
def on_slider_change(val):
    print(f"Slider changed to {val:.2f}")
gui.add(Label((20, 70, 130, 30), "Volume:"))
slider = Slider((160, 75, 300, 20), 0, 100, 50, on_slider_change)
gui.add(slider)

# === CheckBox ===
def on_checkbox_toggle(state):
    print(f"Checkbox is now {'checked' if state else 'unchecked'}")
checkbox = CheckBox((160, 120, 20, 20), "Accept Terms", callback=on_checkbox_toggle)
gui.add(checkbox)

# === Dropdown ===
def on_dropdown_select(option):
    print(f"Dropdown selected: {option}")
gui.add(Label((20, 160, 130, 30), "Choose Fruit:"))
dropdown = Dropdown((160, 160, 200, 30), ["Apple", "Banana", "Cherry"], callback=on_dropdown_select)
gui.add(dropdown)

# === Main Loop ===
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
