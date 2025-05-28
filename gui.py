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
class Slider(Widget):
    def __init__(self, rect, min_val, max_val, initial, callback=None):
        super().__init__(rect)
        self.min = min_val
        self.max = max_val
        self.value = initial
        self.callback = callback
        self.knob_rect = pygame.Rect(0, 0, 10, rect[3])
        self.dragging = False
        self.update_knob_pos()

    def update_knob_pos(self):
        ratio = (self.value - self.min) / (self.max - self.min)
        self.knob_rect.centerx = self.rect.x + int(ratio * self.rect.w)
        self.knob_rect.centery = self.rect.centery

    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), self.rect)
        pygame.draw.rect(surface, (200, 200, 200), self.knob_rect)
        val_text = FONT.render(f"{self.value:.2f}", True, (255, 255, 255))
        surface.blit(val_text, (self.rect.right + 10, self.rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.knob_rect.collidepoint(event.pos):
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            x = min(max(event.pos[0], self.rect.x), self.rect.x + self.rect.w)
            ratio = (x - self.rect.x) / self.rect.w
            self.value = self.min + ratio * (self.max - self.min)
            self.update_knob_pos()
            if self.callback:
                self.callback(self.value)
        return False
    
class CheckBox(Widget):
    def __init__(self, rect, text, checked=False, callback=None):
        super().__init__(rect)
        self.checked = checked
        self.callback = callback
        self.text = text
        self.box_rect = pygame.Rect(rect[0], rect[1], rect[3], rect[3])

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.box_rect, 2)
        if self.checked:
            pygame.draw.line(surface, (255, 255, 255), self.box_rect.topleft, self.box_rect.bottomright, 2)
            pygame.draw.line(surface, (255, 255, 255), self.box_rect.topright, self.box_rect.bottomleft, 2)
        txt_surf = FONT.render(self.text, True, (255, 255, 255))
        surface.blit(txt_surf, (self.box_rect.right + 10, self.box_rect.y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.box_rect.collidepoint(event.pos):
            self.checked = not self.checked
            if self.callback:
                self.callback(self.checked)
        return False


class Dropdown(Widget):
    def __init__(self, rect, options, callback=None):
        super().__init__(rect)
        self.options = options
        self.selected = options[0] if options else ''
        self.expanded = False
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), self.rect)
        txt = FONT.render(self.selected, True, (255, 255, 255))
        surface.blit(txt, (self.rect.x + 5, self.rect.y + 5))

        if self.expanded:
            for i, opt in enumerate(self.options):
                opt_rect = pygame.Rect(self.rect.x, self.rect.bottom + i * self.rect.height, self.rect.w, self.rect.h)
                pygame.draw.rect(surface, (60, 60, 60), opt_rect)
                opt_txt = FONT.render(opt, True, (255, 255, 255))
                surface.blit(opt_txt, (opt_rect.x + 5, opt_rect.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.expanded = not self.expanded
            elif self.expanded:
                for i, opt in enumerate(self.options):
                    opt_rect = pygame.Rect(self.rect.x, self.rect.bottom + i * self.rect.height, self.rect.w, self.rect.h)
                    if opt_rect.collidepoint(event.pos):
                        self.selected = opt
                        self.expanded = False
                        if self.callback:
                            self.callback(opt)
                        break
                else:
                    self.expanded = False
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

