#Sprite: A compter graphic term for an object that can move around the screen (eg: Mario)

import pygame
import random
#Will help to setup folders
import os 

#Set the window
WIDTH = 800
HEIGHT = 600

#FPS: In how much time the screen will be updated
FPS = 30

#Initialize pygame
pygame.init()

#Initialize music
pygame.mixer.init()

#Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set caption
pygame.display.set_caption("My First Game")

#Make clock
clock = pygame.time.Clock()

#Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#setup assests folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder , "Image")

class Player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        #Make it move in x direction
        self.rect.x += 5
        #Not let it go out of the screen
        if self.rect.left > WIDTH:
            self.rect.right = 0

#A group for all sprites
all_sprites = pygame.sprite.Group()
#Player object
player =  Player()
all_sprites.add(player)
#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #Process input (events) 
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
    #Updates
    all_sprites.update()
    #Draw/render

    screen.fill(BLACK)
    all_sprites.draw(screen)
    #Double buffering(After drawing everything flip the display)
    pygame.display.flip()