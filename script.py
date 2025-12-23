# Example file showing a circle moving on screen
import pygame
from random import randint

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
speedy = 0
speedx = 0
air = True
playerspeed = 600
friction = 0.8
enimspeed = 5

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
enim_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() -80)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan")

    pygame.draw.circle(screen, "blue", enim_pos, 400)
    pygame.draw.circle(screen, "green", player_pos, 40)
    pygame.draw.circle(screen, "red", player_pos, 30)
    pygame.draw.circle(screen, "blue", player_pos, randint(9,11))
    pygame.draw.circle(screen, "red", enim_pos, 40)

    diff = player_pos - enim_pos
    if diff.magnitude() < 400:
        if enim_pos.x < player_pos.x:
            enim_pos.x += enimspeed
        else:
            enim_pos.x -= enimspeed
        if enim_pos.y < player_pos.y:
            enim_pos.y += enimspeed
        else:
            enim_pos.y -= enimspeed

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_pos.y > 600:
        speedy = -20
        player_pos.y += speedy
    if keys[pygame.K_a] and (player_pos.y > 600 or air):
        speedx = -playerspeed * dt
    if keys[pygame.K_d] and (player_pos.y > 600 or air):
       speedx = playerspeed * dt
    if player_pos.y < 620:
        player_pos.y += speedy
        speedy += 1
    else:
        speedy = -1
    player_pos.x += speedx
    if player_pos.y > 600:
        speedx = speedx * friction
    if keys[pygame.K_r] or diff.magnitude() < 70 :
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        enim_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2 )

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()