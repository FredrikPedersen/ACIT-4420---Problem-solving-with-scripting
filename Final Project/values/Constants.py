# Animations
ANIMATIONS_ENABLED: bool = True

# Window Constants
WINDOW_WIDTH: int = 840
WINDOW_HEIGHT: int = 840

# Grid Constants
GRID_WIDTH: int = 5
GRID_HEIGHT: int = 5

# Maze Constants
ROOT_X: int = 20
ROOT_Y: int = 20
CELL_SIZE: int = 20
MAZE_WIDTH: int = ((GRID_WIDTH - 1) * CELL_SIZE) + ROOT_X
MAZE_HEIGHT: int = ((GRID_HEIGHT - 1) * CELL_SIZE) + ROOT_Y


def set_grid_width(value: int):
    global GRID_WIDTH
    GRID_WIDTH = value
    __update_maze_width()


def set_grid_height(value: int):
    global GRID_HEIGHT
    GRID_HEIGHT = value
    __update_maze_height()


def __update_maze_width():
    global MAZE_WIDTH, GRID_WIDTH, ROOT_X
    MAZE_WIDTH = ((GRID_WIDTH - 1) * CELL_SIZE) + ROOT_X


def __update_maze_height():
    global MAZE_HEIGHT, GRID_HEIGHT, ROOT_Y
    MAZE_HEIGHT = ((GRID_HEIGHT - 1) * CELL_SIZE) + ROOT_Y
