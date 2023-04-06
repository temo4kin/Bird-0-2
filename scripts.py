import pygame, sys


def events(bird, tubes):
    '''
    Отслеживание событий в игре
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Завершение программы в', pygame.time.get_ticks()/1000)
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:

            # Нажатие клавиши 'p' для запуска программы

            if event.key == pygame.K_p:
                print('Запуск программы в', pygame.time.get_ticks()/1000)
                bird.game_start = True
                tubes.start_tube = True

            # нажатие клавиши "пробел" для подъёма птички

            if event.key == pygame.K_SPACE:
                bird.bird_up = True

            # остановка программы на паузу по нажатию клавиши "ESC"

            elif event.key == pygame.K_ESCAPE:
                bird.pause = 1
                bird.flag_pause = True

def paused(bird):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                bird.flag_pause = False
                bird.pause = 0