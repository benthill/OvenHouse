import pygame
import time
import sys
from pygame import font


# ONE: make the screen stay on until the user clicks the next button
# TWO: make the text center
def text_ani(str, tuple,line_space,basicfont,screen):
    x, y = tuple
    y = y * line_space ##shift text down by one line
    char = ''        ##new string that will take text one char at a time. Not the best variable name I know.
    letter = 0
    count = 0
    for i in range(len(str)):
        pygame.event.clear() ## this is very important if your event queue is not handled properly elsewhere. Alternativly pygame.event.pump() would work.
        time.sleep(0.05)

        char = char + str[letter]
        text = basicfont.render(char, False, (254, 254, 254), (0, 0, 0)) #First tuple is text color, second tuple is background color
        textrect = text.get_rect(topleft=(x, y)) ## x, y's provided in function call. y coordinate amended by line height where needed
        textrect.center = (800/2), (textrect[1] + 600/3)

        screen.blit(text, textrect)
        pygame.display.update(textrect) ## update only the text just added without removing previous lines.
        count += 1
        letter += 1

def blink_text(str, tuple, rgb,line_space,screen,basicfont):
    pygame.event.clear()
    time.sleep(0.20)

    x, y = tuple
    y = y * line_space

    text = basicfont.render(str, False, rgb, (0, 0, 0))
    textrect = text.get_rect(topleft=(x, y))
    textrect.center = (800/2), (textrect[1] + 600/3)

    screen.blit(text, textrect)
    pygame.display.update(textrect)


def main():
    pygame.init()
    screen = pygame.display.set_mode([800,600])
    line_space = 32

    basicfont = pygame.font.Font('8bitoperator.ttf', 16)
    text_ani('You thought that the witch was the evil character', (0, 1), line_space,basicfont,screen)
    text_ani('who chased you so that she could gobble you up...', (0, 2),line_space,basicfont,screen)
    text_ani("but she WASN'T!", (0, 3),line_space,basicfont,screen)
    text_ani('You have destroyed her lovely house and invaded it,', (0, 4),line_space,basicfont,screen)
    text_ani('and the witch was simply trying to kick you out…', (0, 5),line_space,basicfont,screen)
    text_ani('You now are an outlaw! Ayy', (0, 6),line_space,basicfont,screen)
    text_ani('PRESS SPACEBAR TO PROCEED', (0, 8),line_space,basicfont,screen)

    while True:
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 8), (254,254,254),line_space,screen,basicfont)
        blink_text('PRESS SPACEBAR TO PROCEED', (0, 8), (0,0,0),line_space, screen,basicfont)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
