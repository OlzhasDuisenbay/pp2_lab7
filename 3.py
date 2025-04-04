import pygame
pygame.init()

monitor = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PP2 Pygame")

x = 400
y = 200
speed = 20

check = True

while check:
    monitor.fill("White")
    pygame.draw.circle(monitor, 'Red', (x, y), 25)
    pygame.display.update()

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x - speed > 0 + 20:
            x -= speed
        if keys[pygame.K_RIGHT] and x + speed < 800 - 20:
            x += speed
        if keys[pygame.K_UP] and y - speed > 0 + 20:
            y -= speed
        if keys[pygame.K_DOWN] and y + speed < 400 - 20:
            y += speed

        pygame.draw.circle(monitor, 'Red', (x, y), 25)
        pygame.display.update()
