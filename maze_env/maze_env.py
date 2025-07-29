class MazeEnv:
    def __init__(self, maze, start, goal):
        self.maze = maze                    # 0 = free, 1 = wall. This must be a matrix
        self.start = start                  # (row, column)
        self.goal = goal                    # (row, column)
        self.height = len(maze)
        self.width = len(maze[0])
        self.agent_pos = list(start)        # current agent position

    def reset(self):
        self.agent_pos = list(self.start)
        return self.get_state()

    def get_state(self):
        return tuple(self.agent_pos)

    def step(self, action):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dy, dx = directions[action]
        y, x = self.agent_pos
        ny, nx = y + dy, x + dx

        if 0 <= ny < self.height and 0 <= nx < self.width and self.maze[ny][nx] == 0:
            self.agent_pos = [ny, nx]
            reward = 0.01  
        else:
            reward = -0.7  

        done = (self.agent_pos == list(self.goal))
        if done:
            reward = 4 

        return self.get_state(), reward, done