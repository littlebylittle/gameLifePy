import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, owner, position, color=(0xaf, 0xaf, 0xaf),):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.image = pygame.Surface([owner.square_size - 1,
                                     owner.square_size - 1])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position[0], position[1]

if __name__ == '__main__':
    pass