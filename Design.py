"""
holds information about the design of a page
"""
import pygame
from Constants import *

class Design:

    def __init__(self) -> None:
        self.background = None
        self.color = (255,255,255)
        self.bigFont = pygame.font.Font(f'assets/font/vermin_vibes.otf', 50)
        self.smallFont = pygame.font.Font(f'assets/font/vermin_vibes.otf', 20)
        self.setBackground('starry')

    # show functions
    def showBackground(self, surface):
        surface.blit(self.background, (0,0))
    
    def showText(self, font, text, centerx, centery, surface):

        text = font.render(text, True, self.color)
        rect = text.get_rect()
        rect.center = (centerx, centery)
        surface.blit(text, rect)
    
    def showPage(self, page, surface):
        self.showBackground(surface)

        # home page
        if page == 'home':
            self.showText(self.bigFont, 'ChessNow', 445, 100, surface)

        elif page == 'key':
            self.showText(self.smallFont, 'R:  Reset Board', 445, 280, surface)
            self.showText(self.smallFont, 'Z:  Undo Move', 445, 320, surface)
        
        elif page == 'settings':
            self.showText(self.bigFont, 'Settings', 445, 100, surface)
        
        elif page == 'piece':
            pass

    # set methods
    def setBackground(self, bg_name):
        image = pygame.transform.scale(pygame.image.load(f'assets/background/{bg_name}.jpg'), (BOARD_HEIGHT + MOVELOG_PANEL_WIDTH, BOARD_HEIGHT))
        self.background = image        
    
