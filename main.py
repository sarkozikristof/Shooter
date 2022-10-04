import pygame as pg
from settings import *
from player import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.new_game()


    def new_game(self):
        self.player = Player(self)


    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')
        self.player.update()
    

    def draw(self):
        self.screen.fill('grey')     
        self.player.draw() 


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()


    def run(self):
        while True:
            self.draw()
            self.update()
            self.check_events()



if __name__ == '__main__':
    game = Game()
    game.run()
