import pygame

pygame.init()

FONT = pygame.font.Font(None, 24)

class Widget:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.visible = True
        self.focus = False

    def draw(self, surface):
        pass

    def handle_event(self, event):
        return False

class Button(Widget):
    def __init__(self, rect, text, callback):
        super().__init__(rect)
        self.text = text
        self.callback = callback
        self.hovered = False

    def draw(self, surface):
        color = (200, 100, 100) if self.hovered else (150, 50, 50)
        pygame.draw.rect(surface, color, self.rect, border_radius=5)
        txt_surf = FONT.render(self.text, True, (255, 255, 255))
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hovered and event.button == 1:
                self.callback()
                return True
        return False

class Label(Widget):
    def __init__(self, rect, text, color=(255, 255, 255)):
        super().__init__(rect)
        self.text = text
        self.color = color

    def draw(self, surface):
        txt_surf = FONT.render(self.text, True, self.color)
        surface.blit(txt_surf, self.rect.topleft)

class InputBox(Widget):
    def __init__(self, rect, text=''):
        super().__init__(rect)
        self.text = text
        self.active = False
        self.color_inactive = (100, 100, 100)
        self.color_active = (255, 255, 255)

    def draw(self, surface):
        color = self.color_active if self.active else self.color_inactive
        pygame.draw.rect(surface, color, self.rect, 2)
        txt_surf = FONT.render(self.text, True, color)
        surface.blit(txt_surf, (self.rect.x + 5, self.rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
        return False

class GUIManager:
    def __init__(self):
        self.widgets = []

    def add(self, widget):
        self.widgets.append(widget)

    def handle_event(self, event):
        for widget in self.widgets:
            if widget.visible and widget.handle_event(event):
                break

    def draw(self, surface):
        for widget in self.widgets:
            if widget.visible:
                widget.draw(surface)

# ========== Example Usage ==========

if __name__ == '__main__':
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    running = True

    gui = GUIManager()

    def on_click():
        print("Button Clicked!")

    gui.add(Label((10, 10, 100, 30), "Enter Name:"))
    gui.add(InputBox((120, 10, 200, 30)))
    gui.add(Button((10, 60, 150, 40), "Click Me", on_click))

    while running:
        screen.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            gui.handle_event(event)

        gui.draw(screen)
        pygame.display.flip()
        clock.tick(60)
