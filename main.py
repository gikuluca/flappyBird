import pygame
from pygame.locals import *


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super(Bird, self).__init__()
        self.surf = pygame.image.load("bird.png")
        self.surf = pygame.transform.scale(self.surf,(75,75))
        self.rect = self.surf.get_rect()
        self.isJump = False
        self.jumpCount = 15
        self.fallCount = 30

    def update(self, pressed_keys):
        global SCREEN_H,SCREEN_W
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.y + 75 >= SCREEN_H:
            self.rect.y = SCREEN_H - 75
        if self.rect.y <=0:
            self.rect.y = 0

        if pressed_keys[K_SPACE]:
            self.isJump = True
            self.jumpCount,self.fallCount = 15,30
        if self.isJump:
            if self.jumpCount > 0:
                self.rect.y -= (self.jumpCount**1.5)/4
                self.jumpCount-=1
            elif self.fallCount > 0:
                self.rect.y += (self.fallCount**1.5)/4
                self.fallCount -=1
            else:
                self.isJump=False
                self.jumpCount, self.fallCount = 15, 30


pygame.init()

SCREEN_H = 600
SCREEN_W = 800
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
background = pygame.image.load("background.png")
background = pygame.transform.scale(background,(SCREEN_W,SCREEN_H))
running = True

bird = Bird()


while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    bird.update(pressed_keys)
    screen.blit(bird.surf, bird.rect)
    pygame.display.flip()
    clock.tick(20)
    pygame.display.update()

