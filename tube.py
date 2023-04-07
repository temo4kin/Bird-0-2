import pygame

class Tube(pygame.sprite.Sprite):
    '''
    Класс труб
    '''

    def __init__(self, surf, speed, group, w, h,):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(bottomright=(w, h))
        self.speed = speed
        self.start_tube = False
        self.add(group)
        
    
    def update(self, *args):
        
        if self.start_tube:
            print(self.start_tube)
            if self.rect.right > 0:
                self.rect.x -= self.speed
            else:
                self.kill()