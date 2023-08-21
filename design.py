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
        self.tinyFont = pygame.font.Font('assets/font/vermin_vibes.otf', 18)
        self.mediumFont = pygame.font.Font(f'assets/font/vermin_vibes.otf', 23)
        self.endGameTextFont = pygame.font.Font(f'assets/font/SIXTY.TTF', 50)
        self.setBackground('dark_bg')
        self.messageFont = p.font.Font("assets/font/monofonto rg.otf", 14)

        self.friendlyBotIcon = p.image.load('assets/icons/friendly_icon.png').convert_alpha()
        self.friendlyText = self.smallFont.render('Boop Bot', True, ('#FF5F00'))
        self.friendlyTextbox = p.image.load('assets/icons/textboxes/friendly_textbox.png').convert_alpha()
        self.friendlyBotDescribe1 = self.messageFont.render('Boop doesn\'t', True, ('#803000'))
        self.friendlyBotDescribe2 = self.messageFont.render('need to win.', True, ('#803000'))
        self.friendlyBotDescribe3 = self.messageFont.render('He\'s just', True, ('#803000'))
        self.friendlyBotDescribe4 = self.messageFont.render('happy to play.', True, ('#803000'))
        
        self.evilBotIcon = p.image.load('assets/icons/evil_icon.png').convert_alpha()
        self.evilText = self.smallFont.render('Beep Bot', True, ('#008C5C'))
        self.evilTextbox = p.image.load('assets/icons/textboxes/evil_textbox.png').convert_alpha()
        self.evilBotDescribe1 = self.messageFont.render('Two words.', True, ('#003825'))
        self.evilBotDescribe2 = self.messageFont.render('Humans, beware.', True, ('#003825'))
        
        self.augBotIcon = p.image.load('assets/icons/aug_icon.png').convert_alpha()
        self.augText = self.smallFont.render('Augustine', True, ('#FF003B'))
        self.augTextbox = p.image.load('assets/icons/textboxes/aug_textbox.png').convert_alpha()
        self.augBotDescribe1 = self.messageFont.render('Augustine is', True, ('#470010'))
        self.augBotDescribe2 = self.messageFont.render('an attacker,', True, ('#470010'))
        self.augBotDescribe3 = self.messageFont.render('keep your', True, ('#470010'))
        self.augBotDescribe4 = self.messageFont.render('guard up.', True, ('#470010'))
        
        self.arditBotIcon = p.image.load('assets/icons/ardit_icon.png').convert_alpha()
        self.arditText = self.smallFont.render('Ardit', True, ('#006994'))
        self.arditTextbox = p.image.load('assets/icons/textboxes/ardit_textbox.png').convert_alpha()
        self.arditBotDescribe1 = self.messageFont.render('Ardit defends,', True, ('#003347'))
        self.arditBotDescribe2 = self.messageFont.render('should you do', True, ('#003347'))
        self.arditBotDescribe3 = self.messageFont.render('the same?', True, ('#003347'))
        
        self.abbyBotIcon = p.image.load('assets/icons/abby_icon.png').convert_alpha()
        self.abbyText = self.smallFont.render('Abby', True, ('#CBAC19'))
        self.abbyBotDescribe1 = self.messageFont.render('Abby is a', True, ('#443A08'))
        self.abbyBotDescribe2 = self.messageFont.render('positional player.', True, ('#443A08'))
        self.abbyBotDescribe3 = self.messageFont.render('Place your', True, ('#443A08'))
        self.abbyBotDescribe4 = self.messageFont.render('pieces wisely.', True, ('#443A08'))
        self.abbyTextbox = p.image.load('assets/icons/textboxes/abby_textbox.png').convert_alpha()


        self.friendlyBotIconLost = p.image.load('assets/icons/friendly_defeat_icon.png').convert_alpha()
        self.evilBotIconLost = p.image.load('assets/icons/evil_defeat_icon.png').convert_alpha()
        self.augBotIconLost = p.image.load('assets/icons/aug_defeat_icon.png').convert_alpha()
        self.arditBotIconLost = p.image.load('assets/icons/ardit_defeat_icon.png').convert_alpha()
        self.abbyBotIconLost = p.image.load('assets/icons/abby_defeat_icon.png').convert_alpha()


        self.creatorAugText = self.mediumFont.render('Augustine George', True, ('#C195E4'))
        self.augCredit1Text = self.tinyFont.render('Gameplay Logic', True, ('#C195E4'))
        
        self.creatorAbbyText = self.mediumFont.render('Abby Steele', True, ('#9749D1'))
        self.abbyCredit1Text = self.tinyFont.render('UI', True, ('#9749D1'))
        self.abbyCredit2Text = self.tinyFont.render('Artwork and Design', True, ('#9749D1'))
        
        self.creatorArditText = self.mediumFont.render('Ardit Xhemajli', True, ('#811CDA'))
        self.arditCredit1Text = self.tinyFont.render('AI Opponents', True, ('#811CDA'))


        self.linkedInLabel = self.mediumFont.render('Connect with us', True, ('#ffffff'))

        self.endGameBox = pygame.image.load('assets/gameEndBox.png').convert_alpha()
        self.textBox = pygame.transform.smoothscale(pygame.image.load('assets/textbox.png'), (245, 90)).convert_alpha()
        self.sideScreenBg = pygame.image.load('assets/sideScreenBg.png').convert_alpha()

        # example images

        self.iconDict = {
            'boop': self.friendlyBotIcon,
            'boopLost': self.friendlyBotIconLost,

            'beep': self.evilBotIcon,
            'beepLost': self.evilBotIconLost,

            'augustine': self.augBotIcon,
            'augustineLost': self.augBotIconLost,

            'ardit': self.arditBotIcon,
            'arditLost': self.arditBotIconLost,

            'abby': self.abbyBotIcon,
            'abbyLost': self.abbyBotIconLost,
        }

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
            surface.blit(self.friendlyBotDescribe1, (40,385))
            surface.blit(self.friendlyBotDescribe2, (40,405))
            surface.blit(self.friendlyBotDescribe3, (40,425))
            surface.blit(self.friendlyBotDescribe4, (40,445))

            surface.blit(self.evilTextbox, (200,340))
            surface.blit(self.evilBotDescribe1, (210, 385))
            surface.blit(self.evilBotDescribe2, (210, 405))

            surface.blit(self.augTextbox, (370,340))
            surface.blit(self.augBotDescribe1, (380, 385))
            surface.blit(self.augBotDescribe2, (380, 405))
            surface.blit(self.augBotDescribe3, (380, 425))
            surface.blit(self.augBotDescribe4, (380, 445))

            surface.blit(self.arditTextbox, (540,340))
            surface.blit(self.arditBotDescribe1, (550, 385))
            surface.blit(self.arditBotDescribe2, (550, 405))
            surface.blit(self.arditBotDescribe3, (550, 425))

            surface.blit(self.abbyTextbox, (710,340))
            surface.blit(self.abbyBotDescribe1, (720, 385))
            surface.blit(self.abbyBotDescribe2, (720, 405))
            surface.blit(self.abbyBotDescribe3, (720, 425))
            surface.blit(self.abbyBotDescribe4, (720, 445))
            

        elif page == 'credit':
            self.showBackground(surface)
            team = p.transform.smoothscale(p.image.load('assets/icons/creators.png'), (350,350))
            self.showText(self.bigFont, 'Creators', 445, 60, surface)
            surface.blit(team, (275, 80))
            surface.blit(self.linkedInLabel, (180, 530))

            surface.blit(self.creatorAugText, (75, 345))
            surface.blit(self.augCredit1Text, (75, 390))

            surface.blit(self.creatorAbbyText, (350, 345))
            surface.blit(self.abbyCredit1Text, (430, 420))
            surface.blit(self.abbyCredit2Text, (325, 390))

            surface.blit(self.creatorArditText, (550, 345))
            surface.blit(self.arditCredit1Text, (615, 390))

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
    
    def drawSideScreen(self, screen, imageName, type=''):

        sideSceenRect = p.Rect(BOARD_WIDTH, 0, MOVELOG_PANEL_WIDTH, MOVELOG_PANEL_HEIGHT)
        screen.blit(self.sideScreenBg, (640, 0))
        screen.blit(self.textBox, (645, 160))
        if type == 'Lost':
            screen.blit(self.iconDict[f'{imageName}{type}'], (690, 10))
        else:
            screen.blit(self.iconDict[f'{imageName}'], (690, 10))
        
        messageText = random.choice(MESSAGES[f'{imageName}{type}']) if isinstance(MESSAGES[f'{imageName}{type}'], list) else MESSAGES[f'{imageName}{type}']
        message = self.messageFont.render(messageText, True, (0,0,0))
        messageRect = message.get_rect()
        messageRect.center = (sideSceenRect.centerx, 200)
        screen.blit(message, messageRect)

    def drawEndGameText(self, screen, text):

        screen.blit(self.endGameBox, (10,55))
        font = self.endGameTextFont
        textObject = font.render(text, False, p.Color("gray"))
        textLocation = p.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - textObject.get_width() / 2,
                                                                    BOARD_HEIGHT / 2 - textObject.get_height() / 2)
        screen.blit(textObject, textLocation)
        textObject = font.render(text, True, p.Color('red'))
        screen.blit(textObject, textLocation.move(2, 2))