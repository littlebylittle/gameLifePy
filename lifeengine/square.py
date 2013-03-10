import pygame


class Square(pygame.sprite.Sprite):
    checked_color = (0xff, 0, 0)
    unchecked_color = (0xaf, 0xaf, 0xaf)

    def __init__(self, owner, position,):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.image = pygame.Surface([owner.square_size - 1,
                                     owner.square_size - 1])

        self.image.fill(Square.unchecked_color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position[0], position[1]
        self.checked = False

    def set_color(self, color):
        self.image.fill(color)

    def reverse(self):
        self.checked ^= True
        if self.checked:
            self.set_color(Square.checked_color)
        else:
            self.set_color(Square.unchecked_color)
if __name__ == '__main__':
    pass