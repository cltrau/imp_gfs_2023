# This is a PyGame example of a tileset and rendering tiles.

import pygame
import sys

pygame.init()
fps = 8
timer = pygame.time.Clock()

class Tileset:
    """ Tileset class for loading and storing tiles.
        https://pygame.readthedocs.io/en/latest/tiles/tiles.html
    """

    def __init__(self, file, size=(48, 48), margin=0, spacing=0):
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = []
        self.load()


    def load(self):

        self.tiles = []
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                self.tiles.append(tile)


WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

tileset = Tileset('media/walking-ice-golem-48px.png', (48, 48), 1, 1)
tileset.load()

golem_x = 100
golem_movement = 5
flip_flag = False
tile_index = 0
running = True
while running:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (golem_x > (WIDTH - 50)):
        golem_movement = golem_movement * -1
        flip_flag = True
    if (golem_x < 50):
        golem_movement = golem_movement * -1
        flip_flag = False

    if tile_index >= len(tileset.tiles):
        tile_index = 0

    tile = tileset.tiles[tile_index]
    if flip_flag:
        tile = pygame.transform.flip(tile, True, False)
    screen.blit(tile, (golem_x, 48))
    tile_index += 1
    golem_x += golem_movement

    pygame.display.flip()
    timer.tick(fps)

pygame.quit()
sys.exit()