import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load('')

# Для запуска игры создан цикл while.
# Для удобства завершение НЕ создаем бесконечный цикл while True а создаем для него переменную running
running = True
while running:
    pass  # Пропускаем преждевременное исполнение цикла для исключения синтаксической ошибки

pygame.quit()  # Выход из игры по завершению работы прграммы, когда переменная running станет = False (vs.line 7)
