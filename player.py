import pygame as pg


class Player():
    def __init__(self, game):
        self.game = game
        self.x = 100
        self.y = 100
        self.speed = 2
        self.color = 'white'
        self.radius = 20
        self.mouse_pos = pg.mouse.get_pos()


    def draw(self):
        pg.draw.circle(self.game.screen, self.color, (self.x, self.y), self.radius)
        pg.draw.line(self.game.screen, 'red',(self.x, self.y), (self.mouse_pos), 2)

    def update(self):
        self.mouse_pos = pg.mouse.get_pos()

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.y -= self.speed
        if keys[pg.K_s]:
            self.y += self.speed
        if keys[pg.K_a]:
            self.x -= self.speed
        if keys[pg.K_d]:
            self.x += self.speed