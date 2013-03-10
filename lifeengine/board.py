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

    def __init__(self, resolution=(800, 600), sizes=5):
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

        for i in range(self.number_on_y):
            self.squares.append([])

            for j in range(self.number_on_x):
                position = (j * self.square_size + (Board.border_size // 2),
                            i * self.square_size + (Board.border_size // 2))
                current_square = Square(self, position,)
                self.squares[i].append(current_square)
                self.displayed_sprites.add(current_square)
        #print(self.squares)

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
            self.squares[row][column].reverse()

    def iteration_world(self):
        for i in range(self.number_on_y):
            for j in range(self.number_on_x):

                self.squares[i][j].next = False
                #get 9 neighbors for each cell
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if (0 <= k < self.number_on_y) and (0 <= l < self.number_on_x):
                            population = self.check_square(k, l)
                            if not self.squares[k][l].checked:
                                if population == 3:
                                    self.squares[k][l].next = True
                            elif 3 <= population <= 4:
                                self.squares[k][l].next = True

        for i in range(self.number_on_y):
            for j in range(self.number_on_x):
                if self.squares[i][j].next:
                    self.squares[i][j].set_alive()
                else:
                    self.squares[i][j].set_dead()

    def check_square(self, index_i, index_j):
        population = 0
        if 0 > index_i or index_i > self.number_on_y:
            return 0

        if 0 > index_j or index_j > self.number_on_x:
            return 0
        count = 0
        for i in range(index_i - 1, index_i + 2):
            for j in range(index_j - 1, index_j + 2):
                count += 1
                if 0 <= i < self.number_on_y and 0 <= j < self.number_on_x:
                    population += self.squares[i][j].checked
        return population

    def check_world(self):
        if self.life_in_progress:
            self.iteration_world()
            ##remove that
            #self.life_in_progress ^= True
            ##remove that

    def kill_all(self):
        for i in range(self.number_on_y):
            for j in range(self.number_on_x):
                self.squares[i][j].set_dead()

if __name__ == '__main__':
    pass
    Board()