import pygame
from lifeengine.square import Square


class Board():
    colors = dict()
    colors['red'] = [0xff, 0, 0]
    colors['green'] = [0, 0xff, 0]
    colors['blue'] = [0, 0, 0xff]
    colors['white'] = [0xff, 0xff, 0xff]
    colors['black'] = [0, 0, 0]
    colors['grey'] = [0xf4, 0xe2, 0xd1]
    square_size = 10

    def __init__(self, resolution=(800, 600), sizes=55):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption('Life game:.')
        pygame.mouse.set_visible(True)

        self.width, self.height = resolution
        self.sizes = sizes
        border_size = 50
        min_line_size = min(resolution)
        Board.square_size = min_line_size // sizes
        number_on_x = (resolution[0] - border_size) // Board.square_size
        number_on_y = (resolution[1] - border_size) // Board.square_size

        self.displayed_sprites = pygame.sprite.RenderPlain()

        for i in range(number_on_x):
            for j in range(number_on_y):
                position = (i * Board.square_size + (border_size // 2),
                            j * Board.square_size + (border_size // 2))
                current_square = Square(Board, position, Board.colors['grey'])
                self.displayed_sprites.add(current_square)

    def render(self):
        self.screen.fill(Board.colors['black'])
        self.displayed_sprites.draw(self.screen);
        pygame.display.flip()
        pass


if __name__ == '__main__':
    pass
    Board()