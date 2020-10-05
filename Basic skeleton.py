import pygame
import random

#Set the window
WIDTH = 360
HEIGHT = 480

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
    #Update
    #Draw/render

    screen.fill(BLACK)
    #Double buffering(After drawing everything flip the display)
    pygame.display.flip()
