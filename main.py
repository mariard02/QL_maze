from maze_env import MazeEnv
from render.pygame_renderer import pygame_renderer
from utils import maze_generator

MAZE_SIZE = (31, 31)
START_POS = (1, 1)
CELL_SIZE = 10

def generate_goal_position(rows, cols):
    return (rows - 2, cols - 2)

def setup_maze_environment():
    rows, cols = MAZE_SIZE
    maze_gen = maze_generator.MazeGenerator(rows, cols)
    goal_pos = generate_goal_position(rows, cols)

    return MazeEnv(
        maze=maze_gen.maze,
        start=START_POS,
        goal=goal_pos
    ), maze_gen.maze

if __name__ == "__main__":
    environment, maze = setup_maze_environment()
    
    pygame_renderer(
        maze=maze,
        agent_pos=START_POS,
        goal_pos=environment.goal,
        cell_size=CELL_SIZE
    )