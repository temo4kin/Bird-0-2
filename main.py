import pygame, scripts
from bird import Bird
from tube import Tube
from random import randint


def main():
    pygame.init()
    W, H = 1500, 842

    bg_color = (255, 255, 255)
    font_color = (255, 0, 0)
    text = 'Пауза. Для продолжения игры нажмите ESC или ENTER'
    myfont = pygame.font.Font('Fonts\\ComfortaaMedium.ttf', 36)
    my_text = myfont.render(text, True, font_color)
    
    clock = pygame.time.Clock()
    FPS = 60

    tubes_images = ['tube.png',]
    tubes_surf = [pygame.image.load('Images\\'+path).convert_alpha() for path in tubes_images]

    def createTube(group):
        '''
        Создание групп труб
        '''

        indx = randint(0, len(tubes_surf)-1)
        speed = randint(1, 4)

        return Tube(tubes_surf[indx], speed, group)

    tubes = pygame.sprite.Group()

    screen = pygame.display.set_mode((W, H), flags=pygame.SCALED) #, flags=pygame.NOFRAME)
    pygame.display.set_caption('Jump! 2.0')
    icon = pygame.image.load('Images\\bird.png')
    pygame.display.set_icon(icon)
    
    # блок создания экземпляров классов спрайтов
 
    bird = Bird(screen, W, H)
    print('Программа запущена в', pygame.time.get_ticks()/1000)
    speed = 2
    tubes.add(Tube(screen, W, H, 'Images\\tube.png', speed))

    running = True

    while running:
        scripts.events(bird, tubes)
        screen.fill(bg_color)
        bird.output_bird()
        bird.fall()
        tubes.draw(screen)
        
        if bird.pause == 1:
             while bird.flag_pause:
                pos = my_text.get_rect(center=(W//2, H//2))
                screen.blit(my_text, pos)
                pygame.display.update(pos)
                clock.tick(5)
                scripts.paused(bird)
        pygame.display.flip()
        clock.tick(FPS)
        tubes.update(W)
    
if __name__ == "__main__":
    main()
