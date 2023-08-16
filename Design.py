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

        self.friendlyBotIcon = p.transform.smoothscale(p.image.load('assets/icons/friendly_icon.png'), (150,150))
        self.friendlyText = self.smallFont.render('Boop Bot', True, ('#FF5F00'))
        self.friendlyTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/friendly_textbox.png'), (150,180))
        self.evilBotIcon = p.transform.smoothscale(p.image.load('assets/icons/evil_icon.png'), (150,150))
        self.evilText = self.smallFont.render('Beep Bot', True, ('#008C5C'))
        self.evilTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/evil_textbox.png'), (150,180))
        self.augBotIcon = p.transform.smoothscale(p.image.load('assets/icons/aug_icon.png'), (150,150))
        self.augText = self.smallFont.render('Augustine', True, ('#FF003B'))
        self.augTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/aug_textbox.png'), (150,180))
        self.arditBotIcon = p.transform.smoothscale(p.image.load('assets/icons/ardit_icon.png'), (150,150))
        self.arditText = self.smallFont.render('Ardit', True, ('#006994'))
        self.arditTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/ardit_textbox.png'), (150,180))
        self.abbyBotIcon = p.transform.smoothscale(p.image.load('assets/icons/abby_icon.png'), (150,150))
        self.abbyText = self.smallFont.render('Abby', True, ('#CBAC19'))
        self.abbyTextbox = p.transform.smoothscale(p.image.load('assets/icons/textboxes/abby_textbox.png'), (150,180))
        

    # show functions
    def showBackground(self, surface):
        surface.blit(self.background, (0,0))
    
    def showText(self, font, text, centerx, centery, surface):

        text = font.render(text, True, self.color)
        rect = text.get_rect()
        rect.center = (centerx, centery)
        surface.blit(text, rect)
    
    def showPage(self, page, surface):

        # home page
        if page == 'home':
            self.showBackground(surface)
            logo = p.transform.scale(p.image.load('assets/logo.png'), (100,100))
            surface.blit(logo, (400, 45))
            self.showText(self.bigFont, 'ChessNow', 445, 100, surface)

        elif page == 'pva_select':
            self.showBackground(surface)
            self.showText(self.bigFont, 'Select Opponent', 445, 100, surface)
            # load ins

            surface.blit(self.friendlyBotIcon, (30, 205))
            surface.blit(self.evilBotIcon, (200, 205))
            surface.blit(self.augBotIcon, (370, 205))
            surface.blit(self.arditBotIcon, (540, 205))
            surface.blit(self.abbyBotIcon, (710, 205))
            surface.blit(self.friendlyText, (50,175))
            surface.blit(self.evilText, (220,175))
            surface.blit(self.augText, (385,175))
            surface.blit(self.arditText, (580,175))
            surface.blit(self.abbyText, (750,175))
            surface.blit(self.friendlyTextbox, (30,340))
            surface.blit(self.evilTextbox, (200,340))
            surface.blit(self.augTextbox, (370,340))
            surface.blit(self.arditTextbox, (540,340))
            surface.blit(self.abbyTextbox, (710,340))
        
            

        elif page == 'key':
            self.showBackground(surface)
            self.showText(self.bigFont, 'Keybinds', 445, 100, surface)
            self.showText(self.smallFont, 'R:  Reset Board', 445, 280, surface)
            self.showText(self.smallFont, 'Z:  Undo Move', 445, 320, surface)
        
        elif page == 'settings':
            self.showBackground(surface)
            self.showText(self.bigFont, 'Settings', 445, 100, surface)
        elif page == 'pva':
            pygame.draw.rect(surface, (255,255,255), (640,560,250,80))
        
        elif page == 'piece':
            self.showBackground(surface)
            pass
        elif page == 'board':
            self.showBackground(surface)
            pass
        elif page == 'background':
            self.showBackground(surface)
            pass

    # set methods
    def setBackground(self, bg_name):
        image = pygame.transform.scale(pygame.image.load(f'assets/background/{bg_name}.jpg'), (BOARD_HEIGHT + MOVELOG_PANEL_WIDTH, BOARD_HEIGHT))
        self.background = image        
    
