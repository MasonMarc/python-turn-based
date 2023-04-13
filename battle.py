import pygame

pygame.init()

#game window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


#load images always load assets outside of game loop
#background image
background_img = pygame.image.load('img/Background/background.png').convert_alpha()
#panel image
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

#load background function
def draw_bg():
    screen.blit(background_img, (0,0))

#load panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))

run = True
while run:

    #load bg
    draw_bg()

    #load panel
    draw_panel()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()