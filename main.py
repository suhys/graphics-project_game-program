# Reproduce the Graphics window program in the book:
# INVENT YOUR OWN COMPUTER GAMES with PYTHON
#
#
# YOUR OUTPUT should look like this, and should stay in its own window.  It should NOT just open and close again quickly.
# The code shown in the book above (in chapter 17: Graphics) has all top-level code (code not contained in a function
# It would be better if your code were almost all contained in functions, something like this:
import pygame
import pygame as pg
import sys
from pygame.locals import *


class Game:
    # Set up the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self):
        # Set up pygame
        pg.init()
        # Set up the window
        self.screen = pg.display.set_mode((500, 400), 0, 32)
        pg.display.set_caption('Python Graphics App')
        # Set up the fonts
        self.basic_font = pg.font.SysFont(None, 48)

    def __repr__(self):
        return f'Polygon Graphics Game'

    def update(self):
        pass

    def draw(self):
        pass

    def restart(self):
        pass

    def level_up(self):
        pass

    def save(self):
        pass

    def draw_polygons(self):
        pygame.draw.polygon(self.screen, Game.GREEN, ((146, 0), (291, 106),
                                                      (236, 277), (56, 277), (0, 106)))

    def draw_lines(self):
        pg.draw.line(self.screen, Game.BLUE, (60, 60), (120, 60), 4)
        pg.draw.line(self.screen, Game.BLUE, (120, 60), (60, 120))
        pg.draw.line(self.screen, Game.BLUE, (60, 120), (120, 120))

    def draw_circles(self):
        pg.draw.circle(self.screen, Game.BLUE, (300, 50), 20, 0)
        pg.draw.ellipse(self.screen, Game.RED, (300, 250, 40, 80), 5)

    def draw_text(self):
        text = self.basic_font.render("Hello world!", True, Game.WHITE, Game.BLUE)
        text_rect = text.get_rect()
        text_rect.centerx = self.screen.get_rect().centerx
        text_rect.centery = self.screen.get_rect().centery
        pygame.draw.rect(self.screen, Game.RED, (text_rect.left - 20,
                                                 text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))
        pix_array = pg.PixelArray(self.screen)
        pix_array[480][380] = Game.BLACK
        del pix_array

        self.screen.blit(text, text_rect)

    def draw_objects(self):
        self.draw_polygons()
        self.draw_lines()
        self.draw_circles()
        self.draw_text()

    def play(self):
        finished = False
        while not finished:
            for event in pg.event.get():  # event loop
                self.screen.fill(Game.WHITE)
                self.draw_objects()  # redraws entire screen and objects 60 frames/second
                pg.display.update()

                if event.type == QUIT:
                    pg.quit()
                    sys.exit()


# YOUR CODE HERE  ...

def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
