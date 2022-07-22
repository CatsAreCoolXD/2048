import random
import pygame

pygame.init()

class Board:
    def __init__(self):
        self.tiles = {"row_1": [0,0,0,0], "row_2": [0,0,0,0], "row_3": [0,0,0,0], "row_4": [0,0,0,0]}
        self.rNumber = 2
        self.rRow = 1
        self.rTile = 1
        self.tileIsZero = False
        self.usedTileCount = 0
        self.generated = False
        self.game_over = False

    def get_tile(self, row, index):
        return self.tiles["row_" + str(row)][index]

    def generate(self):
        if random.random() < 0.9:
            self.rNumber = 2
        else:
            self.rNumber = 4

        while not self.tileIsZero and not self.generated and self.usedTileCount < 16:
            self.rRow = random.randint(1,4)
            self.rTile = random.randint(0,3)
            if self.tiles["row_" + str(self.rRow)][self.rTile] == 0:
                self.tiles["row_" + str(self.rRow)][self.rTile] = self.rNumber
                self.generated = True
        self.generated = False

    def check_tiles(self):
        self.usedTileCount = 0
        for x in range(len(self.tiles)):
            for tile in self.tiles["row_" + str(x+1)]:
                if tile > 0:
                    self.usedTileCount += 1
        if self.usedTileCount == 16:
            self.game_over = True

        print(self.usedTileCount)

screen = pygame.display.set_mode((1280, 720))
b = Board()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

game = True
menu = False

r = True
while r:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False

    screen.fill(WHITE)
    if game:
        keys = pygame.key.get_pressed()
        b.check_tiles()
        if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            b.generate()
        if b.game_over:
            menu = True
            game = False
    elif menu:
        pass
    pygame.display.flip()

pygame.quit()


