"""
WRITE YOUR PROGRAM HEADER HERE
"""

import sys, os 
sys.path.append(os.path.dirname(__file__))

from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:

    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object (Stack or Queue)
        self._visited = set()
        self._prev = {}
        self._solution = None

    def tileIsVisitable(self, row, col):
        base = self.maze.makeMazeBase()
        return 0 <= row < len(base) and 0 <= col < len(base[0]) and base[row][col] != '#' and (row, col) not in self._visited
        pass

    def solve(self):
        s = self.maze.start
        g = self.maze.goal
        start = (s.getRow(), s.getCol())
        goal = (g.getRow(), g.getCol())
        self._visited.clear()
        self._prev.clear()
        self._solution = None

        self.ss.add(start)
        self._visited.add(start)

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # N, S, E, W
        while not self.ss.isEmpty():
            r, c = self.ss.remove()
            if (r, c) == goal:
                path = []
                cur = goal
                while cur is not None:
                    path.append(cur)
                    cur = self._prev.get(cur)
                self._solution = list(reversed(path))
                return
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                nxt = (nr, nc)
                if self.tileIsVisitable(nr, nc) and nxt not in self._visited:
                    self._prev[nxt] = (r, c)
                    self._visited.add(nxt)
                    self.ss.add(nxt)
                    
        pass

     # Add any other helper functions you might want here

    def getPath(self):
        return self._solution or []
        pass 

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for r, c in solution:
            output_string[r][c] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()