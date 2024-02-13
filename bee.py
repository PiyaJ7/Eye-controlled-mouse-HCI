import pygame
import sys
import random
from math import *

pygame.init()

width = 1080
height = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bee Catcher")
clock = pygame.time.Clock()
score = 0
white = (230, 230, 230)
darkGray = (40, 55, 71)
font = pygame.font.SysFont("Snap ITC", 35)

#background image
background_image = pygame.image.load("imgs/background.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

#bee image
bee_image = pygame.image.load("imgs/bee.png")

#background music
pygame.mixer.music.load("music/Komiku_-_12_-_Bicycle.mp3")
pygame.mixer.music.set_volume(0.5)

#slap sound
slap_sound = pygame.mixer.Sound("music/slap.wav")

#scream sound
scream_sound = pygame.mixer.Sound("music/screaming.wav")

class Bee:
    def __init__(self):
        self.a = random.randint(60, 80)
        self.b = self.a + random.randint(0, 20)
        self.x = random.randint(0, width - self.a)
        self.y = random.randint(0, height - self.b)

    def move(self):
        pass

    def show(self):
        display.blit(pygame.transform.scale(bee_image, (self.a, self.b)), (self.x, self.y))

    def burst(self):
        global score
        pos = pygame.mouse.get_pos()
        if onBee(self.x, self.y, self.a, self.b, pos):
            score += 1
            slap_sound.play()
            pygame.time.delay(500)
            scream_sound.play()
            self.reset()

    def reset(self):
        self.a = random.randint(60, 80)
        self.b = self.a + random.randint(0, 20)
        self.x = random.randint(0, width - self.a)
        self.y = random.randint(0, height - self.b)

bees = []
noBee = 10
