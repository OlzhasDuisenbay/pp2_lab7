"""Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key.
The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored"""
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PP2 Pygame")

x, y = WIDTH // 2, HEIGHT // 2
radius = 25
speed = 20

running = True
while running:
    screen.fill("White")
    pygame.draw.circle(screen, "Red", (x, y), radius)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - speed >= radius:
        x -= speed
    if keys[pygame.K_RIGHT] and x + speed <= WIDTH - radius:
        x += speed
    if keys[pygame.K_UP] and y - speed >= radius:
        y -= speed
    if keys[pygame.K_DOWN] and y + speed <= HEIGHT - radius:
        y += speed

pygame.quit()
