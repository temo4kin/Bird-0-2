import pygame, sys

class Bird():
    def __init__(self, screen, w, h):
        '''
        Создание класса птички
        '''

        self.screen = screen
        self.image = pygame.image.load('Images\\bird.png').convert_alpha()
        self.rect = self.image.get_rect(centerx = (w//5), centery = h//2)
        self.screen_rect = screen.get_rect()
        self.game_start = False
        self.bird_up = False
        self.flag_pause = False
        self.pause = 0

    def output_bird(self):
        '''
        Вывод на экран птички
        '''

        self.screen.blit(self.image, self.rect)

    def fall(self):
        '''
        Падение птицы вниз и подъём вверх по нажатию пробела
        '''

        if self.game_start:
            self.rect.centery += 2
            if self.bird_up:
                self.rect.centery -= 40
                self.bird_up = False
            elif self.rect.bottom > self.screen_rect.bottom:
                print('Game over!')
                pygame.quit()
                sys.exit()
            elif self.rect.top < self.screen_rect.top:
                self.pause = 1
                print('Game over!')
                pygame.quit()
                sys.exit()