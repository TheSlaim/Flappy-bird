import pygame
import random


# Ініціалізація Pygame
pygame.init()

# Параметри екрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Кольори
WHITE = (255, 255, 255)
BLUE = (0, 191, 255)
GREEN = (0, 255, 0)

# Гравець
bird_image = pygame.image.load('images/bird.png')
wall_image = pygame.image.load('images/wall.png')
background_image = pygame.image.load('images/background.png')
bird = pygame.Rect(100, HEIGHT // 2, 30, 30)
gravity = 0
jump = -10

# Труби
pipe_width = 70
pipe_gap = 150
pipes = []
pipe_speed = 3
for i in range(3):
    x = WIDTH + i * 200
    y = random.randint(100, HEIGHT - 200)
    pipes.append(pygame.Rect(x, y, pipe_width, HEIGHT - y))
    pipes.append(pygame.Rect(x, 0, pipe_width, y - pipe_gap))

# Змінна для рахунку
score = 0

# Головний цикл гри
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gravity = jump

    # Гравітація
    bird.y += gravity
    gravity += 1

    # Рух труб
    for pipe in pipes:
        pipe.x -= pipe_speed
        if pipe.right < 0:
            pipes.remove(pipe)
            if pipe.y == 0:
                x = max([p.x for p in pipes]) + 200
                y = random.randint(100, HEIGHT - 200)
                pipes.append(pygame.Rect(x, y, pipe_width, HEIGHT - y))
                pipes.append(pygame.Rect(x, 0, pipe_width, y - pipe_gap))
                score += 1

    # Відображення об'єктів
    pygame.draw.rect(screen, BLUE, bird)
    screen.blit(bird_image, (bird.x-8, bird.y-8))
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    # Колізія
    if bird.top < 0 or bird.bottom > HEIGHT or any(bird.colliderect(pipe) for pipe in pipes):
        print(f"Гра закінчена! Ваш рахунок: {score}")
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
