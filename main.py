# This file was created by: Ryder Magobet

# passionate about cars, and racing
# make racing game
# Final Project Name: Cuttin' up
# Goals:
# move, drive fast, cut up, cool colors, turns, extoic cars, paved roads...etc.

import pygame
from pygame.locals import *
import random

pygame.init()

# create the window
width = 500
height = 500
screen_size = (width, height)
screen = pygame.display.set_mode (screen_size)
pygame.display.set_caption('Car Game')

# colors
gray = (100,100,100)
green = (76,208,56)
red = (200,0,0)
white = (255,255,255)
yellow = (255,232,0)


# game settings

gameover = False
speed = 2
score = 0

# marker size
marker_width = 20
marker_height = 50

# road and edge markers
road = (100,0,300, height)
left_edge_marker = (95,0, marker_width,height)
right_edge_marker = (395,0, marker_width, height)


#  x coordinates of lanes
left_lane = 150
center_lane = 250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# for animating movement of lane markers
lane_marker_move_y = 0

class Vehicle(pygame.sprite.Sprite): 
    

    def _init_(self,image, x,y):
        pygame.sprite.Sprite._init_(self)

        # scale the image down so it fits in the lane
        image_scale = 45 / image.get_rect().width
        new_width = image.get.rect().width * image_scale
        new_height = image.get.rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('Car.png')
        super().__init__(image, x, y)

# players starting coordinates 
player_x= 250
player_y=400


# create players car
player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)


# game loop
clock = pygame.time.Clock()
fps = 60
running = True
while running:

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


        # draw the grass
        screen.fill(green)

        # draw the road
        pygame.draw.rect(screen, gray, road)

        # draw the edge marker
        pygame.draw.rect(screen, yellow, left_edge_marker)
        pygame.draw.rect(screen, yellow, right_edge_marker)

        # draw lane markers
        lane_marker_move_y += speed * 2
        if lane_marker_move_y >= marker_height * 2:
            lane_marker_move_y = 0
        for y in range(marker_height * -2, height, marker_height * 2):
            pygame.draw.rect(screen, white, (left_lane +45, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen, white, (center_lane + 45, y +lane_marker_move_y, marker_width, marker_height))

            # draw players car
            player_group.draw(screen)






        pygame.display.update()

