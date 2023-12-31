# This file was created by: Ryder Magobet

# Goals
# Speed gets faster and faster
# Fun
# Difficult but not too hard
# Have other cars on the road
# Use code I have never used before


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# settings
width = 600
height = 400
car_width = 50
car_height = 80
enemy_width = 50
enemy_height = 80
speed = 5
score = 0


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
grey = (128,128,128)



# game over feture
# gives fonts and sets game over
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Game Over", True, white)
game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2))

# Create the game window
# creates the size of windw and its name
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Game")

# Load images, specific to my game
car_image = pygame.image.load("Car.png")  
enemy_image = pygame.image.load("enemy.png")




# Player car class
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        # int gives the numbers for the function
        super().__init__()
        # suoper alows the main car to have prioity 
        self.image = pygame.transform.scale(car_image, (car_width, car_height))
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height - 50)

# lets the player move with left and right arrows
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += speed

# Enemy car class
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_image, (enemy_width, enemy_height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - enemy_width)
        self.rect.y = random.randint(-height, -enemy_height)

# sets the speed qand how many enemys are coming
    def update(self):
        self.rect.y += speed
        if self.rect.y > height:
            self.rect.x = random.randint(0, width - enemy_width)
            self.rect.y = random.randint(-height, -enemy_height)

# oil spill sprite
class OilSpill(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("oil_spill.png")  # Replace with your oil spill image file
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5  # Adjust the speed as needed
# spawns it in randomly
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > height:
            self.rect.y = random.randint(-height, -self.rect.height)
            self.rect.x = random.randint(0, width - self.rect.width)


# Create sprite groups
            # lets the sprites run
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()



# Create player car
player_car = PlayerCar()
all_sprites.add(player_car)

# Create initial enemy cars
# 5 cars set each loop
for _ in range(5):  
    enemy_car = EnemyCar()
    all_sprites.add(enemy_car)
    enemies.add(enemy_car)

# Game loop
clock = pygame.time.Clock()
# 60 fps for speed of game
fps = 60

while True:
    # when cars come into contact with enemys closes game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    all_sprites.update()
# resets score and finishes game
    for enemy_car in enemies:
        if enemy_car.rect.bottom > player_car.rect.bottom:
            score += 1

    # Check for collisions with enemy cars
    if pygame.sprite.spritecollide(player_car, enemies, False):
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()
        # has to be in 2000 miliseconds
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting
        pygame.quit()
        sys.exit()

            

    # Draw the backround (grey)
    screen.fill(grey)
    all_sprites.draw(screen)

    # score of game as cars pass the player
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))
    

    # Refresh the screen
    # flip is a method that updates the full display surface with the contents of the drawing. 
    # It essentially swaps the contents of the display surface with the contents of the drawing buffer.
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)
