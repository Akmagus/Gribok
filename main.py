import pygame
import sys
from random import *
from sounds import *
pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Comic Sans', 30)
start_text_1 = font.render('Добро пожаловать!', False, (255, 0, 0))
start_text_2 = font.render('Нажмите пробел, чтобы начать.', False, (255, 0, 0))

end_text_1 = font.render('Вы прошли игру! Нажмите пробел,', False, (0, 255, 0))
end_text_2 = font.render('чтобы начать заново.', False, (0, 255, 0))

class Sprite:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img_orig = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img_orig, (w, h)) 
        self.direction = "none"

    def move(self):
        if self.direction == "right":
            self.rect.x += 5
        elif self.direction == "left":
            self.rect.x -= 5
        elif self.direction == "up":
            self.rect.y -= 5
        elif self.direction == "down":
            self.rect.y += 5

    def draw(self):
        screen.blit(self.img, self.rect)

player = Sprite(400, 400, 50, 50, "grib.png")
enemy = Sprite(50, 50, 40, 40, "mario.png")
krest = Sprite(10, 10, 30, 30, 'krest.png')

bg_music()

game_state = 0
while True:
    screen.fill((255, 255, 255))
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    game_state = 1
        screen.blit(start_text_1, (20, 225))
        screen.blit(start_text_2, (20, 255))

    if game_state == 2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player.rect.x, player.rect.y, player.rect.width, player.rect.height = 400, 400, 50, 50
                    enemy.rect.x, enemy.rect.y = 50, 50
                    player.img = pygame.transform.scale(player.img_orig, (player.rect.width, player.rect.height))
                    game_state = 1
        screen.blit(end_text_1, (5, 225))
        screen.blit(end_text_2, (5, 255))

    if game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    player.direction = 'right'
                elif e.key == pygame.K_LEFT:
                    player.direction = 'left'
                elif e.key == pygame.K_UP:
                    player.direction = 'up'
                elif e.key == pygame.K_DOWN:
                    player.direction = 'down'
            if e.type == pygame.KEYUP:
                player.direction = 'none'
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if player.rect.x < x < player.rect.right and player.rect.y < y < player.rect.bottom:
                    player.orig_img = pygame.image.load('creeper.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                if 0 < x < 30 and 0 < y < 30:
                    sys.exit()

        player.move()

        if player.rect.colliderect(enemy.rect):
            enemy.rect.x = randint(0, 470)
            enemy.rect.y = randint(0, 470)
            player.rect.width += 5
            player.rect.height += 5
            player.img = pygame.transform.scale(player.img_orig, (player.rect.width, player.rect.height))
            amam()


        if player.rect.width >= 500:
            game_state = 2
            
        player.draw()
        enemy.draw()
        krest.draw()
    pygame.display.update()
    clock.tick(75)