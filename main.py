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


# Функція для екрану очікування
def wait_for_space():
    waiting = True
    font = pygame.font.Font(None, 36)
    while waiting:
        screen.fill(BLUE)
        text = font.render("Press space for start", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


# Головний цикл гри
running = True
clock = pygame.time.Clock()

# Додаємо музику
pygame.mixer.music.load('images/music.mp3')


# Створюємо font
font = pygame.font.Font(None, 36)

# Викликаємо екран очікування
wait_for_space()

pygame.mixer.music.play(-1)
end = False
end2 = False
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
    screen.blit(bird_image, (bird.x - 8, bird.y - 8))
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

    # Виводимо текст на екран
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    # Колізія
    if bird.top < 0 or bird.bottom > HEIGHT or any(bird.colliderect(pipe) for pipe in pipes):
        print(f"Гра закінчена! Ваш рахунок: {score}")
        running = False
        end = True
    if score == 999:
        print("Тобі не набридло?")
        running = False
        end2 = True


    pygame.display.flip()
    clock.tick(30)



font = pygame.font.Font(None, 36)
while end == True:
    screen.fill(BLUE)
    Theend = font.render(f"You lose, your score: {score}", True, WHITE)
    screen.blit(Theend, (WIDTH // 2 - Theend.get_width() // 2, HEIGHT // 2 - Theend.get_height() // 2))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            end = False

while end2 == True:
    screen.fill(BLUE)
    Theend2 = font.render("Aren't you bored?", True, WHITE)
    screen.blit(Theend2, (WIDTH // 2 - Theend2.get_width() // 2, HEIGHT // 2 - Theend2.get_height() // 2))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            end2 = False

pygame.quit()
