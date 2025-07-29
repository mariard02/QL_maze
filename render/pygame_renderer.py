import pygame

def pygame_renderer(maze, agent_pos=None, goal_pos=None, cell_size=20):
    """
    Render a maze using pygame, showing walls, paths, agent, and goal.
    
    Args:
        maze (list of list of int): Maze matrix (1 = wall, 0 = path).
        agent_pos (tuple of int): (row, col) position of the agent. Painted red.
        goal_pos (tuple of int): (row, col) position of the goal. Painted blue.
        cell_size (int): Size in pixels of each maze cell.
    """
    pygame.init()

    rows = len(maze)
    cols = len(maze[0])

    screen_width = cols * cell_size
    screen_height = rows * cell_size

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze")

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # White background

        for i in range(rows):
            for j in range(cols):
                color = (0, 0, 0) if maze[i][j] == 1 else (255, 255, 255)
                rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, color, rect)

        # Draw agent in red if given
        if agent_pos:
            ai, aj = agent_pos
            rect = pygame.Rect(aj * cell_size, ai * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 0, 0), rect)

        # Draw goal in blue if given
        if goal_pos:
            gi, gj = goal_pos
            rect = pygame.Rect(gj * cell_size, gi * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 0, 255), rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


# Example usage:
if __name__ == "__main__":
    maze = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,1,1,0,1],
        [1,0,0,1,0,1],
        [1,1,0,0,0,1],
        [1,1,1,1,1,1],
    ]
    agent_pos = (1,1)
    goal_pos = (4,4)
    pygame_renderer(maze, agent_pos, goal_pos, cell_size=40)
