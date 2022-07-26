import random
import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = position
        self.used_for_score = False

    @staticmethod
    def randomPipe(cfg, image):
        base_y = 0.79 * cfg.SCREEN_HEIGHT
        up_y = int(base_y * 0.2) + random.randrange(0, int(base_y * 0.60 - cfg.PIPE_GAP_SIZE))

        return {'top': (cfg.SCREEN_WIDTH + 10, up_y - image.get_height),
                'bottom': (cfg.SCREEN_WIDTH + 10, up_y + cfg.PIPE_GAP_SIZE)}
