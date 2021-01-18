import pygame, os

pygame.font.init()

WIN_WIDTH = 1200
WIN_HEIGHT = 700
win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption('Chicken Invaders by Mates')

class Background(object):
    img = pygame.image.load(os.path.join("imgs", "BG.jpg"))
    velocity = 8
    flipped_img =pygame.transform.flip(img, False, True)
    height = img.get_height()

    def __init__(self):
        self.y1 = 0
        self.y2 = self.height * -1
        self.x = 0


    def move(self):
        self.y1 += self.velocity
        self.y2 += self.velocity

        if self.y1 >= self.height:
            self.y1 = self.height * -1
        if self.y2 >= self.height:
            self.y2 = self.height * -1

    def draw(self, win):
        win.blit(self.img, (self.x, self.y1))
        win.blit(self.flipped_img, (self.x, self.y2))

class Drawer(object):
    def __init__(self):
        self.bg = Background()

    def redraw(self):
        win.fill((255, 255, 0))
        self.bg.draw(win)
        pygame.draw.rect(win,(255,0,0),(10,10,50,50))
        # self.bg.move()