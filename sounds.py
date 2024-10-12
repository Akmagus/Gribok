import pygame

def bg_music():
    pygame.mixer.music.load('sounds/flipflap.mp3')
    pygame.mixer.music.play(-1)

def amam():
    amam = pygame.mixer.Sound('sounds/amam.mp3')
    amam.play()