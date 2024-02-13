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

for i in range(noBee):
    obj = Bee()
    bees.append(obj)

def onBee(x, y, a, b, pos):
    return x < pos[0] < x + a and y < pos[1] < y + b

def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = (255, 255, 255)
    pygame.draw.ellipse(display, color, (pos[0] - r / 2, pos[1] - r / 2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l / 2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l / 2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l / 2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l / 2, pos[1]), (pos[0] - l, pos[1]), 4)

def lowerPlatform():
    pygame.draw.rect(display, darkGray, (0, height - 100, width, 100))

def showScore():
    scoreText = font.render("Bees Caught: " + str(score), True, white)
    display.blit(scoreText, (150, height - 70))

def close():
    pygame.quit()
    sys.exit()

def game():
    global score
    pygame.mixer.music.play(-1)
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noBee):
                    bees[i].burst()

        display.blit(background_image, (0, 0))
        for i in range(noBee):
            bees[i].show()
        pointer()
        lowerPlatform()
        showScore()
        pygame.display.update()
        clock.tick(60)

game()