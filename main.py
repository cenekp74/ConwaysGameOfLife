import pygame

WIDTH = 1200
HEIGHT = 1000
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
GREEN = (0, 230, 30)
SPEED = 10
FPS = 60

PARENT_DIR = ""

PAUSE = pygame.image.load(PARENT_DIR+"/"+"textures/pause.png")
PLAY = pygame.image.load(PARENT_DIR+"/"+"textures/play.png")


class Grid:
    def __init__(self, points) -> None:
        self.grid = [['+' for i in range(100)] for i in range(100)]
        for point in points:
            self.grid[point[0]][point[1]] = '.'

    def __repr__(self) -> str:
        s = ''
        for row in self.grid:
            for col in row:
                s += col + ' '
            s += '\n'
        return s
    
    def tick(self) -> None:
        new_grid = [['+' for i in range(100)] for i in range(100)]
        for rowI, row in enumerate(self.grid):
            for colI, col in enumerate(row):
                neighbours = 0
                if rowI+1 < 100:
                    if self.grid[rowI+1][colI] != '+': neighbours += 1
                if rowI-1 >= 0:
                    if self.grid[rowI-1][colI] != '+': neighbours += 1
                if colI+1 < 100:
                    if self.grid[rowI][colI+1] != '+': neighbours += 1
                if colI-1 >= 0:
                    if self.grid[rowI][colI-1] != '+': neighbours += 1
                if rowI+1 < 100 and colI+1 < 100:
                    if self.grid[rowI+1][colI+1] != '+': neighbours += 1
                if rowI+1 < 100 and colI-1 >= 0:
                    if self.grid[rowI+1][colI-1] != '+': neighbours += 1
                if rowI-1 >= 0 and colI+1 < 100:
                    if self.grid[rowI-1][colI+1] != '+': neighbours += 1
                if rowI-1 >= 0 and colI-1 >= 0:
                    if self.grid[rowI-1][colI-1] != '+': neighbours += 1

                if self.grid[rowI][colI] != '+':
                    if neighbours == 2 or neighbours == 3:
                        new_grid[rowI][colI] = '.'
                else:
                    if neighbours == 3:
                        new_grid[rowI][colI] = '.'
        self.grid = new_grid

    def draw(self, win):
        for rowI, row in enumerate(self.grid):
            for colI, col in enumerate(row):
                color = GREEN if col != '+' else BLUE
                pygame.draw.rect(win, color, pygame.Rect(colI*10, rowI*10, 9, 9))

if __name__ == '__main__':
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.init()
    grid = Grid([])
    run = True
    play = False
    frame_number = 0 
    clock = pygame.time.Clock()

    while run:
        frame_number += 1
        WIN.fill((0, 0, 0))
        clock.tick(FPS)
        grid.draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid.grid[int(y/10)][int(x/10)] = '.' if grid.grid[int(y/10)][int(x/10)] == '+' else '+'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play
                elif event.key == pygame.K_c:
                    grid.grid = [['+' for i in range(100)] for i in range(100)]

        if play:
            if frame_number%(FPS/SPEED) == 0:
                grid.tick()
            WIN.blit(PAUSE, (1075, 800))
        else:
            WIN.blit(PLAY, (1075, 800))
            
        pygame.display.update()
