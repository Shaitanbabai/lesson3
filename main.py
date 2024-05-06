import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('Images/Icon.jpg')
pygame.display.set_icon(icon)

target_image = pygame.image.load('Images/target3.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Начальные скорости движения мишени
target_speed_x = 2
target_speed_y = 2

color = (random.randint(a=0, b=255), random.randint(a=0, b=255), random.randint(a=0, b=255))


# Для запуска игры создан цикл while.
# Для удобства завершение НЕ создаем бесконечный цикл while True а создаем для него переменную running
running = True
while running:
    screen.fill(color)  # Задаем цвета экрана
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Пауза после попадания
                pygame.time.delay(1000)
                # Перемещение мишени в новое случайное место
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

            # Обновление положения мишени
        target_x += target_speed_x
        target_y += target_speed_y

        # Обработка столкновения с краями экрана
        if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
            target_speed_x = -target_speed_x
        if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
            target_speed_y = -target_speed_y

        screen.blit(target_image, (target_x, target_y))
        pygame.display.update()

pygame.quit()  # Выход из игры по завершению работы прграммы, когда переменная running станет = False (vs.line 7)
