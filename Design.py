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
        self.setBackground('dark_bg')

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
            logo = p.transform.scale(p.image.load('assets/logo.png'), (100,100))
            surface.blit(logo, (400, 45))
            self.showText(self.bigFont, 'ChessNow', 445, 100, surface)

        elif page == 'pva_select':
            self.showText(self.bigFont, 'Select Opponent', 445, 100, surface)
            # load ins
            friendlyBotIcon = p.transform.smoothscale(p.image.load('assets/icons/friendly_icon.png'), (150,150))
            friendlyText = self.smallFont.render('Boop Bot', True, ('#FF5F00'))
            friendlyTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/friendly_textbox.png'), (150,180))
            evilBotIcon = p.transform.smoothscale(p.image.load('assets/icons/evil_icon.png'), (150,150))
            evilText = self.smallFont.render('Beep Bot', True, ('#008C5C'))
            evilTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/evil_textbox.png'), (150,180))
            augBotIcon = p.transform.smoothscale(p.image.load('assets/icons/aug_icon.png'), (150,150))
            augText = self.smallFont.render('Augustine', True, ('#FF003B'))
            augTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/aug_textbox.png'), (150,180))
            arditBotIcon = p.transform.smoothscale(p.image.load('assets/icons/ardit_icon.png'), (150,150))
            arditText = self.smallFont.render('Ardit', True, ('#006994'))
            arditTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/ardit_textbox.png'), (150,180))
            abbyBotIcon = p.transform.smoothscale(p.image.load('assets/icons/abby_icon.png'), (150,150))
            abbyText = self.smallFont.render('Abby', True, ('#CBAC19'))
            abbyTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/abby_textbox.png'), (150,180))

            surface.blit(friendlyBotIcon, (30, 205))
            surface.blit(evilBotIcon, (200, 205))
            surface.blit(augBotIcon, (370, 205))
            surface.blit(arditBotIcon, (540, 205))
            surface.blit(abbyBotIcon, (710, 205))
            surface.blit(friendlyText, (50,175))
            surface.blit(evilText, (220,175))
            surface.blit(augText, (385,175))
            surface.blit(arditText, (580,175))
            surface.blit(abbyText, (750,175))
            surface.blit(friendlyTextbox, (30,340))
            surface.blit(evilTextbox, (200,340))
            surface.blit(augTextbox, (370,340))
            surface.blit(arditTextbox, (540,340))
            surface.blit(abbyTextbox, (710,340))
        
            

        elif page == 'key':
            self.showText(self.smallFont, 'R:  Reset Board', 445, 280, surface)
            self.showText(self.smallFont, 'Z:  Undo Move', 445, 320, surface)
        
        elif page == 'settings':
            self.showText(self.bigFont, 'Settings', 445, 100, surface)
        
        elif page == 'piece':
            pass
        elif page == 'board':
            pass
        elif page == 'background':
            pass

    # set methods
    def setBackground(self, bg_name):
        image = pygame.transform.scale(pygame.image.load(f'assets/background/{bg_name}.jpg'), (BOARD_HEIGHT + MOVELOG_PANEL_WIDTH, BOARD_HEIGHT))
        self.background = image        
    
