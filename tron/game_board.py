import pygame
import numpy as np
 
class GameBoard:
    def __init__(self, width, height):
        """
        Initialize the game board.
        :param width: Width of the game board in grid cells
        :param height: Height of the game board in grid cells
        """
        # TODO: Initialize a 2D list to represent the game board
        # 0 can represent empty cells, 1 for player trails
        pygame.init()
        self.width=width
        self.height = height
        self.grid = list(np.zeros((height, width)))
    
    def draw(self, screen):
        """
        Draw the game board on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Iterate through the 2D list and draw rectangles for each cell
        # Empty cells can be one color, trails another
        
        for i in range(self.height):
            for j in range(self.width):
                if(self.grid[i][j] == 1):                     
                    pygame.draw.rect(screen, (0, 255, 0), (i, j, 1, 1) )
    
    
    def is_collision(self, x, y):
        """
        Check if the given coordinates collide with the board boundaries or a trail.
        :param x: X-coordinate to check
        :param y: Y-coordinate to check
        :return: True if collision, False otherwise
        """
        # TODO: Check if x and y are within board boundaries
        # Also check if the cell at (x, y) is not empty (i.e., has a trail)
        return not (0 <= x < self.width and 0 <= y < self.height and self.grid[x][y] == 0)