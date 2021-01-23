"""quiditch.py is a simple quiditch inspired game using pygame. """
import pygame as pg
import time
import random

# globals
WIDTH = 1000
HEIGHT = 800
FPS = 60
SCORE = 0
TIME = 0  # number of frames since the start of the game
LAST_QUAFFLE_TIME = -1000  # number of frames when the last quaffle was caught

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# initialize pg and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Movement Example")
clock = pg.time.Clock()


class Player(pg.sprite.Sprite):
    """class that contains Harry Potter"""
    def __init__(self):
        width = 300
        height = 500
        x = 0
        y = 0
        self.spritesheet = pg.image.load("hp.png").convert()
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        """this function is called every times there is a new frame
           it checks whether any of the the arrow keys are being pressed
           and moves Harry Potter."""
        self.vx, self.vy = 0, 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vy = -5
        if keystate[pg.K_DOWN]:
            self.vy = 5
        if keystate[pg.K_LEFT]:
            self.vx = -5
        if keystate[pg.K_RIGHT]:
            self.vx = 5
        if self.vx != 0 and self.vy != 0:
            self.vx /= 1.414
            self.vy /= 1.414
        self.rect.x = (self.rect.x+self.vx) % WIDTH
        self.rect.y = (self.rect.y+self.vy) % HEIGHT


class Bludger(pg.sprite.Sprite):
    """this class contains the bludger and the bludger moves randomly."""
    def __init__(self, vx=2, vy=-2, start_x=1/5, start_y=2/5):
        width = 220
        height = 229
        x = 0
        y = 0
        self.spritesheet = pg.image.load("bludger.jpg").convert()
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH * start_x, HEIGHT * start_y)
        self.vx, self.vy = vx, vy

    def update(self):
        """this function is called every frame. it randomises the velocity of the bludger."""
        rand = random.randint(0, 100)
        if rand <= 1:
            self.vx = -self.vx
            self.vy = -self.vy
        if 1 < rand <= 2:
            self.vx = -self.vx
            self.vy = self.vy
        if 2 < rand <= 3:
            self.vx = self.vx
            self.vy = -self.vy
        self.rect.x = (self.rect.x+self.vx) % WIDTH
        self.rect.y = (self.rect.y+self.vy) % HEIGHT


class Snitch(pg.sprite.Sprite):
    def __init__(self):
        width = 288
        height = 175
        x = 0
        y = 0
        self.spritesheet = pg.image.load("snitch.jpg").convert()
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 2, height // 2))
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3 * 2, HEIGHT / 4 * 3)
        self.vx, self.vy = 3, 3

    def update(self):
        rand = random.randint(0, 100)
        if rand <= 2:
            self.vx = -self.vx
            self.vy = -self.vy
        if 2 < rand <= 4:
            self.vx = -self.vx
            self.vy = self.vy
        if 4 < rand <= 5:
            self.vx = self.vx
            self.vy = -self.vy
        self.rect.x=(self.rect.x+self.vx)%WIDTH
        self.rect.y=(self.rect.y+self.vy)%HEIGHT

class Quaffle(pg.sprite.Sprite):
    def __init__(self):
        width=512
        height=512
        x=0
        y=0
        self.spritesheet = pg.image.load("quaffle.png").convert()
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image, (width // 4, height // 4))
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 3 * 2, HEIGHT / 4 * 3)
        self.vx, self.vy = 3, 3

    def update(self):
        rand = random.randint(0, 100)
        if rand <= 2:
            self.vx = -self.vx
            self.vy = -self.vy
        if 2 < rand <= 4:
            self.vx = -self.vx
            self.vy = self.vy
        if 4 < rand <= 5:
            self.vx = self.vx
            self.vy = -self.vy
        self.rect.x=(self.rect.x+self.vx)%WIDTH
        self.rect.y=(self.rect.y+self.vy)%HEIGHT

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
bludger = Bludger()
all_sprites.add(bludger)
bludger2 = Bludger(vx=-1, vy=3, start_x=1/3, start_y=5/6)
all_sprites.add(bludger2)
snitch = Snitch()
all_sprites.add(snitch)
quaffle = Quaffle()
all_sprites.add(quaffle)
# Game loop
running = True
while running:
    TIME += 1
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if player.rect.colliderect(bludger.rect) or player.rect.colliderect(bludger2.rect):

            pg.font.init()  # you have to call this at the start,
            # if you want to use this module.
            myfont = pg.font.SysFont('georgia', 50)
            textsurface = myfont.render('oh dear you have been hit by a bludger ', True, BLACK)
            screen.blit(textsurface, (WIDTH / 10, HEIGHT / 2))
            pg.display.flip()
            time.sleep(5)
            running = False

        if player.rect.colliderect(snitch.rect):
            pg.font.init()  # you have to call this at the start,
            # if you want to use this module.
            myfont = pg.font.SysFont('georgia', 50)
            textsurface = myfont.render('well done, you have caught the snitch!', True, BLACK)
            screen.blit(textsurface, (WIDTH/10, HEIGHT/2))
            pg.display.flip()
            time.sleep(5)
            print("congratulations, you have won!")
            running = False
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
    if player.rect.colliderect(quaffle.rect):
        if TIME - LAST_QUAFFLE_TIME > 600:
            SCORE += 10
            LAST_QUAFFLE_TIME = TIME
    # Update
    all_sprites.update()
    screen.fill(WHITE)
    myfont = pg.font.SysFont('georgia', 15)
    textsurface = myfont.render('Score: ' + str(SCORE), True, BLACK)
    screen.blit(textsurface, (WIDTH / 10, HEIGHT / 10))
    pg.display.flip()
    # Draw / render
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()
print(pg.font.get_fonts())
