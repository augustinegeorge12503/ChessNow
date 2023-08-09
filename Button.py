"""
creates a button
"""
import pygame

class Button:

    def __init__(self, text, font, text_color, button_color, size, pos, screen) -> None:
        
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.size = size
        self.pos = pos
        self.screen = screen

        self.button_rect = pygame.Rect(0,0,self.size[0], self.size[1])
        self.button_rect.center = pos
        self.text_surf = self.font.render(self.text, True, self.text_color)
        text_width, text_height = self.text_surf.get_size()
        self.text_rect = pygame.Rect(0,0,text_width,text_height)
        self.text_rect.center = ((self.button_rect.right + self.button_rect.left) // 2, (self.button_rect.top + self.button_rect.bottom) // 2)

        self.button_color_absolute = self.button_color
        self.text_color_absolute = self.text_color

    def draw(self):

        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_color = self.text_color_absolute
            self.text_color = self.button_color_absolute
        else:
            self.button_color = self.button_color_absolute
            self.text_color = self.text_color_absolute

        pygame.draw.rect(self.screen, self.button_color, self.button_rect, 0, 15)
        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.screen.blit(self.text_surf, self.text_rect)
    
    def check_collision(self):
        return self.button_rect.collidepoint(pygame.mouse.get_pos())
        