# 🎮 Py-GUI
> A lightweight and intuitive Pygame GUI library

## ✨ Features

- 🔲 **Button** - Clickable buttons with hover effects
- 📝 **InputBox** - Text input fields
- 🏷️ **Label** - Simple text display
- 🎚️ **Slider** - Adjustable value control
- ☑️ **Checkbox** - Toggle options
- 📝 **Dropdown** - Selection from multiple options

## 🚀 Quick Start

```python
import pygame
from gui import GUIManager, Button

pygame.init()
screen = pygame.display.set_mode((400, 200))
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
```

## 📚 Components

### Button
```python
Button((x, y, width, height), "Button Text", callback_function)
```

### InputBox
```python
InputBox((x, y, width, height), "Initial Text")
```

### Slider
```python
Slider((x, y, width, height), min_value, max_value, initial_value, callback_function)
```

### Checkbox
```python
CheckBox((x, y, width, height), "Checkbox Text", initial_state, callback_function)
```

### Dropdown
```python
Dropdown((x, y, width, height), ["Option1", "Option2", "Option3"], callback_function)
```

## 🔍 Examples

Check out the `examples` folder for complete demonstrations of each component:
- `button.py` - Button demonstration
- `textinput.py` - Input box usage
- `Slider.py` - Slider control
- `checkbox` - Checkbox implementation
- `dropdown.py` - Dropdown menu
- `all.py` - Complete showcase of all widgets

## 🛠️ Requirements

- Python 3.x
- Pygame

## 📄 License

MIT License

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
