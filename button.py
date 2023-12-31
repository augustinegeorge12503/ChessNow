"""
creates a button
"""
import pygame
from sound import Sound

class Button:

    def __init__(self, text, font, textColor, buttonColor, size, pos, screen, square=False, selected=False) -> None:
        
        self.text = text
        self.font = font
        self.textColor = textColor
        self.buttonColor = buttonColor
        self.size = size
        self.pos = pos
        self.screen = screen
        self.selected = selected

        self.buttonRect = pygame.Rect(0,0,self.size[0], self.size[1])
        self.buttonRect.center = pos
        self.textSurf = self.font.render(self.text, True, self.textColor)
        textWidth, text_height = self.textSurf.get_size()
        self.textRect = pygame.Rect(0,0,textWidth,text_height)
        self.textRect.center = ((self.buttonRect.right + self.buttonRect.left) // 2, (self.buttonRect.top + self.buttonRect.bottom) // 2)

        self.buttonColorAbsolute = self.buttonColor
        self.textColorAbsolute = self.textColor
        self.sound = Sound('assets/sounds/click1.wav')
        self.square = square

    def draw(self):

        if not self.selected :
            if self.buttonRect.collidepoint(pygame.mouse.get_pos()):
                self.buttonColor = self.textColorAbsolute
                self.textColor = self.buttonColorAbsolute
            else:
                self.buttonColor = self.buttonColorAbsolute
                self.textColor = self.textColorAbsolute
        else:
            self.buttonColor = self.textColorAbsolute
            self.textColor = self.buttonColorAbsolute
                

        if not self.square:
            pygame.draw.rect(self.screen, self.buttonColor, self.buttonRect, 0, 15)
        else:
            pygame.draw.rect(self.screen, self.buttonColor, self.buttonRect)
        self.textSurf = self.font.render(self.text, True, self.textColor)
        self.screen.blit(self.textSurf, self.textRect)
    
    def checkCollision(self):
        return self.buttonRect.collidepoint(pygame.mouse.get_pos())
    
    def changeSelection(self):
        self.selected = True

    def isSelected(self):
        return self.selected
    
    def playClickSound(self):
        self.sound.play()