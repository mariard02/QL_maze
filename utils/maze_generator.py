import random

class MazeClass:
    def __init__(self, rows, cols):
        """
        Initialize the maze grid with all walls.
        
        Parameters:
        rows (int): Number of rows in the maze.
        cols (int): Number of columns in the maze.
        
        The maze is represented as a 2D list where:
        - 1 represents a wall.
        - 0 represents a path.
        """
        self.rows = rows
        self.cols = cols
        # Create a 2D grid filled with walls (value 1)
        self.maze = [[1 for _ in range(self.cols)] for _ in range(self.rows)]

    def create_maze(self, x, y):
        """
        Recursive function to generate the maze using
        randomized depth-first search (backtracking).
        
        Starting from the cell at (x, y), carve paths by
        knocking down walls between cells.
        
        Moves in 4 possible directions by jumping 2 cells
        at a time to avoid immediate neighbors (which are walls).
        
        Parameters:
        x (int): Current row position.
        y (int): Current column position.
        """
        # Directions: up, down, left, right by 2 cells
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)  # Randomize directions for varied mazes

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check if new cell (nx, ny) is inside maze boundaries
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                # If the new cell is still a wall, it means unvisited
                if self.maze[nx][ny] == 1:
                    # Remove wall between current cell and new cell
                    self.maze[x + dx // 2][y + dy // 2] = 0
                    # Mark new cell as a path
                    self.maze[nx][ny] = 0
                    # Recursively generate maze from new cell
                    self.create_maze(nx, ny)

class MazeGenerator:
    def __init__(self, rows, cols):
        """
        Initializes the MazeGenerator by creating a MazeClass instance,
        setting the starting point, and generating the maze.
        
        Parameters:
        rows (int): Number of rows in the maze.
        cols (int): Number of columns in the maze.
        """
        maze_class = MazeClass(rows, cols)
        maze = maze_class.maze

        # Starting position (usually odd coordinates to avoid boundary walls)
        start_x, start_y = 1, 1

        # Mark the starting cell as a path
        maze[start_x][start_y] = 0

        # Generate the maze starting from the start cell
        maze_class.create_maze(start_x, start_y)

        # Save the generated maze for external access
        self.maze = maze

# Example: print the generated maze to console
if __name__ == "__main__":
    mg = MazeGenerator(15, 15)
    for row in mg.maze:
        # Print '#' for walls and space ' ' for paths
        print(''.join(['#' if cell == 1 else ' ' for cell in row]))