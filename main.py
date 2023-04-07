import pygame, scripts, os
from bird import Bird
from tube import Tube
from random import randint

def main():

    def createTube(group):
        '''
        Создание групп труб
        '''

        indx = randint(0, len(tubes_surf)-1)
        speed = randint(1, 4)

        return Tube(tubes_surf[indx], speed, group, W, H)
    
    pygame.init()
    W, H = 1500, 842
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    game_dir = os.path.dirname(__file__)
    images_dir = os.path.join(game_dir, 'Images')
    fonts_dir = os.path.join(game_dir, 'Fonts')


    bg_color = (255, 255, 255)
    font_color = (255, 0, 0)
    text = 'Пауза. Для продолжения игры нажмите ESC или ENTER'
    myfont = pygame.font.Font(os.path.join(fonts_dir, 'ComfortaaMedium.ttf'), 36)
    my_text = myfont.render(text, True, font_color)
    
    clock = pygame.time.Clock()
    FPS = 60

    screen = pygame.display.set_mode((W, H), flags=pygame.SCALED) #, flags=pygame.NOFRAME)
    pygame.display.set_caption('Jump! 2.0')
    icon = pygame.image.load(os.path.join(images_dir, 'bird.png'))
    pygame.display.set_icon(icon)

    tubes_images = ['tube.png',]
    tubes_surf = [(pygame.image.load(os.path.join(images_dir, path)).convert_alpha()) for path in tubes_images]

    tubes = pygame.sprite.Group()

    # блок создания экземпляров классов спрайтов
 
    bird = Bird(screen, W, H)

    print('Программа запущена в', pygame.time.get_ticks()/1000)
    speed = 2
    #tubes.add(Tube(screen, W, H, 'Images\\tube.png', speed))

    running = True
    
    createTube(tubes)

    while running:
        scripts.events(bird, tubes)
        screen.fill(bg_color)
        bird.output_bird()
        tubes.draw(screen)
        bird.fall()
        tubes.update(speed) # Метод не работает в данный момент - не запускается в начале игры. 
                            # Как выяснил это связано с тем, что у группы спрайтов нет такой переменной. 
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                print('Создание второй трубы')
                createTube(tubes)
        
        
        if bird.pause == 1:
             while bird.flag_pause:
                pos = my_text.get_rect(center=(W//2, H//2))
                screen.blit(my_text, pos)
                pygame.display.update(pos)
                clock.tick(5)
                scripts.paused(bird)
        pygame.display.flip()
        clock.tick(FPS)
        
    
if __name__ == "__main__":
    main()
