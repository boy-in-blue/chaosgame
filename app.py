import pygame
import numpy as np
from app2 import Pygamer, BLUE, YELLOW, BLACK, BLUER
from random import choice

SIZE = WIDTH, HEIGHT = 1000, 1000
CHUNK = 10
FPS = 9999


class SnakeGamer(Pygamer):
    def __init__(self):
        super().__init__()
        self.points = []
        self.turtle = (0, 0)

    def create_board_matrix(self):
        self.board = np.zeros((WIDTH//CHUNK, HEIGHT//CHUNK), np.int8)
        return self.board

    def create_point(self, rand_points: int = 3):
        for i in range(rand_points):

            self.points.append((np.random.randint(0, WIDTH//CHUNK), np.random.randint(0, WIDTH//CHUNK)))

    def randomize_turtle(self):
        self.turtle = (np.random.randint(0, WIDTH//CHUNK), np.random.randint(0, WIDTH//CHUNK))

    def chaos(self, dist_to_go: float = 0.5):
        a = choice(self.points)
        midpoint = (int((a[0] + self.turtle[0]) * dist_to_go), int((a[1] + self.turtle[1]) * dist_to_go))
        self.board[midpoint] = 1
        self.turtle = midpoint

    def draw_points(self):
        a = np.where(self.board)
        for i in zip(a[0], a[1]):
            for w in range(CHUNK):
                for h in range(CHUNK):
                    self.screen.set_at((CHUNK*i[0]+w, CHUNK*i[1]+h), BLACK)

        for i in self.points:
            for w in range(CHUNK):
                for h in range(CHUNK):
                    self.screen.set_at((CHUNK*i[0]+w, CHUNK*i[1]+h), BLUER)


if __name__ == '__main__':
    pgr = SnakeGamer()
    pgr.start(SIZE)
    pgr.create_board_matrix()
    pgr.create_point(5)
    pgr.randomize_turtle()
    while pgr.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pgr.running = False
            elif event.type == pygame.KEYDOWN:
                pgr.kill_switch(event.key, [pygame.K_ESCAPE, pygame.K_CAPSLOCK])
        pgr.draw_background(BLUE)
        pgr.chaos()
        pgr.draw_points()
        pygame.display.update()
        # pgr.clock.tick(FPS)
