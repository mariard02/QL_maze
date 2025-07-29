from maze_env import MazeEnv
from render.pygame_renderer import pygame_renderer
from utils import maze_generator
import agent
import time

MAZE_SIZE = (15, 15)
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

    current_agent = agent.build_agent()
    network = agent.build_network(2, 4)

    agent.train_dqn(current_agent, environment)

    current_agent.epsilon = 0.0

    environment.reset()

    path = agent.get_agent_path(current_agent, environment)

    pygame_renderer(
        maze=maze,
        agent_path=path,
        goal_pos=environment.goal,
        cell_size=CELL_SIZE
    )
