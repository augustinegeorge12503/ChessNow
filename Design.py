"""
holds information about the design of a page
"""
import pygame
from Constants import *

class Design:

    def __init__(self) -> None:
        self.background = None
        self.color = (255,255,255)
        self.big_font = pygame.font.Font(f'assets/font/vermin_vibes.otf', 50)
        self.small_font = pygame.font.Font(f'assets/font/vermin_vibes.otf', 20)
        self.set_background('starry')

    # show functions
    def show_background(self, surface):
        surface.blit(self.background, (0,0))
    
    def show_text(self, font, text, centerx, centery, surface):

        text = font.render(text, True, self.color)
        rect = text.get_rect()
        rect.center = (centerx, centery)
        surface.blit(text, rect)
    
    def show_page(self, page, surface):
        self.show_background(surface)

        # home page
        if page == 'home':
            self.show_text(self.big_font, 'ChessNow', 376, 100, surface)

        elif page == 'key':
            self.show_text(self.small_font, 'R:  Reset Board', 376, 220, surface)
            self.show_text(self.small_font, 'Z:  Undo Move', 376, 260, surface)

    # set methods
    def set_background(self, bg_name):
        image = pygame.transform.scale(pygame.image.load(f'assets/background/{bg_name}.jpg'), (BOARD_HEIGHT + MOVE_LOG_PANEL_WIDTH, BOARD_HEIGHT))
        self.background = image        
    
