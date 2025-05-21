import pygame as pg
import constants as c

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HIGHT))
pg.display.set_caption("Skylocke Tower Defense")

run = True
while run:
    clock.tick(c.FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()

