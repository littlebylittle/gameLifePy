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
    border_size = 50

    def __init__(self, resolution=(800, 600), sizes=155):
        self.life_in_progress = False
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption('Life game:.')
        pygame.mouse.set_visible(True)

        self.width, self.height = resolution
        self.sizes = sizes

        min_line_size = min(resolution)
        self.square_size = min_line_size // sizes
        self.number_on_x = (resolution[0] - Board.border_size) // self.square_size
        self.number_on_y = (resolution[1] - Board.border_size) // self.square_size

        self.displayed_sprites = pygame.sprite.RenderPlain()
        self.squares = []

        for i in range(self.number_on_x):
            self.squares.append([])

            for j in range(self.number_on_y):
                position = (i * self.square_size + (Board.border_size // 2),
                            j * self.square_size + (Board.border_size // 2))
                current_square = Square(self, position,)
                self.squares[i].append(current_square)
                self.displayed_sprites.add(current_square)
        print(self.squares)

    def render(self):
        self.screen.fill(Board.colors['black'])
        self.displayed_sprites.draw(self.screen)
        pygame.display.flip()
        pass

    def clicked(self, position):
        x, y = position
        x -= Board.border_size // 2
        y -= Board.border_size // 2
        column = x // self.square_size
        row = y // self.square_size

        if (0 <= column < self.number_on_x) and (0 <= row < self.number_on_y):
            self.squares[column][row].reverse()


if __name__ == '__main__':
    pass
    Board()