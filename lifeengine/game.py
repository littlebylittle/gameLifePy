import pygame
from lifeengine.board import Board


class Game():
    size = (40, 40,)
    resolution = (1024, 768,)
    tick_period = 1

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.resolution)

        self.game_board = Board(resolution=Game.resolution)
        self.flag_is_life = False
        self.game_finish = False
        pass

    def _event_handler(self, event_list):
        for event in event_list:
            if event.type == pygame.QUIT:
                self.game_finish = True
                pygame.quit()
                exit()
        pass

    def main(self):
        while self.game_finish is False:
            Game._event_handler(self, pygame.event.get())
            pass
            self.game_board.render()
            self.clock.tick(Game.tick_period)
        pygame.quit()


def main():
    Game().main()

if __name__ == '__main__':
    Game().main()
    pass