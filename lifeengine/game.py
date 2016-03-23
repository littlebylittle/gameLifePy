import pygame
from lifeengine.board import Board


class Game():
    max_square_size = 30
    resolution = (640, 480,)
    tick_period = 550

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.resolution)

        self.game_board = Board(resolution=Game.resolution,
                                sizes=Game.max_square_size)

        self.EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.EVENT, 500)

        self.flag_is_life = False
        self.game_finish = False
        pass

    def _event_handler(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONUP:
                position = pygame.mouse.get_pos()
                self.game_board.clicked(position)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_board.life_in_progress = not self.game_board.life_in_progress
                if event.key == pygame.K_q:
                    self.game_board.kill_all()

            if event.type == pygame.QUIT:
                self.game_finish = True
                pygame.quit()
                exit()
            if event.type == self.EVENT:
                pass
                self.game_board.check_world()
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