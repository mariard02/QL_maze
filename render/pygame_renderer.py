import pygame
import sys
import time

def pygame_renderer(maze, agent_path, goal_pos, cell_size=25, delay=0.15):
    pygame.init()

    rows, cols = len(maze), len(maze[0])
    width, height = cols * cell_size, rows * cell_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("DQN Maze Agent")

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def draw_grid():
        for y in range(rows):
            for x in range(cols):
                rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if maze[y][x] == 1:
                    pygame.draw.rect(screen, black, rect)
                else:
                    pygame.draw.rect(screen, white, rect)
                pygame.draw.rect(screen, black, rect, 1)

    def draw_agent(pos):
        y, x = pos
        rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, blue, rect)

    def draw_goal():
        y, x = goal_pos
        rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, green, rect)

    # Draw initial state
    draw_grid()
    draw_goal()
    draw_agent(agent_path[0])
    pygame.display.flip()

    # Animate the path
    for pos in agent_path[1:]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_grid()
        draw_goal()
        draw_agent(pos)
        pygame.display.flip()
        time.sleep(delay)

    # Wait until user closes
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
