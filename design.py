"""
holds information about the design of a page

"""
import pygame
from constants import *
import random

class Design:

    def __init__(self) -> None:
        self.background = None
        self.color = (255,255,255)
        self.bigFont = pygame.font.Font(f'assets/font/vermin_vibes.otf', 50)
        self.smallFont = pygame.font.Font(f'assets/font/vermin_vibes.otf', 20)
        self.mediumFont = pygame.font.Font(f'assets/font/vermin_vibes.otf', 23)
        self.setBackground('dark_bg')
        self.messageFont = p.font.SysFont("Arial", 14, False, False)

        self.friendlyBotIcon = p.image.load('assets/icons/friendly_icon.png')
        self.friendlyText = self.smallFont.render('Boop Bot', True, ('#FF5F00'))
        self.friendlyTextbox = p.image.load('assets/icons/textboxes/friendly_textbox.png')
        self.evilBotIcon = p.image.load('assets/icons/evil_icon.png')
        self.evilText = self.smallFont.render('Beep Bot', True, ('#008C5C'))
        self.evilTextbox = p.image.load('assets/icons/textboxes/evil_textbox.png')
        self.augBotIcon = p.image.load('assets/icons/aug_icon.png')
        self.augText = self.smallFont.render('Augustine', True, ('#FF003B'))
        self.augTextbox = p.image.load('assets/icons/textboxes/aug_textbox.png')
        self.arditBotIcon = p.image.load('assets/icons/ardit_icon.png')
        self.arditText = self.smallFont.render('Ardit', True, ('#006994'))
        self.arditTextbox = p.image.load('assets/icons/textboxes/ardit_textbox.png')
        self.abbyBotIcon = p.image.load('assets/icons/abby_icon.png')
        self.abbyText = self.smallFont.render('Abby', True, ('#CBAC19'))
        self.abbyTextbox = p.image.load('assets/icons/textboxes/abby_textbox.png')

        self.friendlyBotIconLost = p.image.load('assets/icons/friendly_defeat_icon.png')
        self.evilBotIconLost = p.image.load('assets/icons/evil_defeat_icon.png')
        self.augBotIconLost = p.image.load('assets/icons/aug_defeat_icon.png')
        self.arditBotIconLost = p.image.load('assets/icons/ardit_defeat_icon.png')
        self.abbyBotIconLost = p.image.load('assets/icons/abby_defeat_icon.png')

        self.creatorText = self.mediumFont.render('Augustine George,  Abby Steele,  Ardit Xhemajli', True, ('#9135F0'))

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
            logo = p.image.load('assets/logo.png')
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
        
            

        elif page == 'credit':
            self.showBackground(surface)
            team = p.transform.smoothscale(p.image.load('assets/icons/creators.png'), (350,350))
            self.showText(self.bigFont, 'Creators', 445, 60, surface)
            surface.blit(team, (275, 80))
            #self.showText(self.smallFont, 'Augustine George,  Abby Steele,  Ardit Xhemajli', 435, 365, surface)
            surface.blit(self.creatorText, (75, 345))

        elif page == 'settings':
            self.showBackground(surface)
            self.showText(self.bigFont, 'Settings', 445, 100, surface)
        elif page == 'pva':
            pass
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
    
    def drawSideScreen(self, screen, imageName, first=False):

        sideSceenRect = p.Rect(BOARD_WIDTH, 0, MOVELOG_PANEL_WIDTH, MOVELOG_PANEL_HEIGHT)
        p.draw.rect(screen, p.Color('black'), sideSceenRect)
        if imageName == 'boop' or imageName == 'boopWon':
            screen.blit(self.friendlyBotIcon, (690, 10))
        elif imageName == 'beep' or imageName == 'beepWon':
            screen.blit(self.evilBotIcon, (690, 10))
        elif imageName == 'augustine' or imageName == 'augustineWon':
            screen.blit(self.augBotIcon, (690, 10))
        elif imageName == 'ardit' or imageName == 'arditWon':
            screen.blit(self.arditBotIcon, (690, 10))
        elif imageName == 'abby' or imageName == 'abbyWon':
            screen.blit(self.abbyBotIcon, (690, 10))
        elif imageName == 'boopLost':
            screen.blit(self.friendlyBotIconLost, (690, 10))
        elif imageName == 'beepLost':
            screen.blit(self.evilBotIconLost, (690, 10))
        elif imageName == 'augustineLost':
            screen.blit(self.augBotIconLost, (690, 10))
        elif imageName == 'arditLost':
            screen.blit(self.arditBotIconLost, (690, 10))
        elif imageName == 'abbyLost':
            screen.blit(self.abbyBotIconLost, (690, 10))
        
        if not first:
            messageText = random.choice(MESSAGES[imageName]) if isinstance(MESSAGES[imageName], list) else MESSAGES[imageName]
            message = self.messageFont.render(messageText, True, (255,255,255))
            messageRect = message.get_rect()
            messageRect.center = (sideSceenRect.centerx, 200)
            screen.blit(message, messageRect)
        else:
            messageText = MESSAGES[f'{imageName}Start']
            message = self.messageFont.render(messageText, True, (255,255,255))
            messageRect = message.get_rect()
            messageRect.center = (sideSceenRect.centerx, 200)
            screen.blit(message, messageRect)
        