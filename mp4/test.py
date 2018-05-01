# import pygame  
# from sys import exit  
# from pygame.locals import QUIT  
# from pygame.locals import KEYDOWN, KEYUP  
# from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN  
  
# background_image_filename = "./images/sushiplate.jpg"  
  
# pygame.init()  
# screen = pygame.display.set_mode((640, 480), 0, 32)  
# background = pygame.image.load(background_image_filename).convert()  
  
# x, y = 0, 0  
# move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}  
  
# while True:  
      
#     for event in pygame.event.get():  
#         if event.type == QUIT:  
#             exit()  
              
#         if event.type == KEYDOWN:  
#             if event.key in move:  
#                 move[event.key] = 1  
#         elif event.type == KEYUP:  
#             if event.key in move:  
#                 move[event.key] = 0  
      
#     x -= move[K_LEFT]  
#     x += move[K_RIGHT]  
#     y -= move[K_UP]  
#     y += move[K_DOWN]  
#     screen.fill((0,0,0))  
#     screen.blit(background, (x, y))  
      
#     pygame.display.update()

background_image_filename ='/Users/haowenjiang/Doc/cs/uiuc/AI/assignment/mp4/sushiplate.jpg'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
SCREEN_SIZE=(640,480)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
background = pygame.image.load(background_image_filename).convert()
x, y =0,0
move_x, move_y =0,0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x =1

            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y =1
            elif event.type == KEYUP:
                move_x =0
                move_y =0
        x += move_x
        y += move_y
        screen.fill((0,0,0))
        screen.blit(background, (x, y))
        pygame.display.update()







