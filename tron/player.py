import numpy as np
import pygame
class Player:
    def __init__(self, x, y, color):
        """
        Initialize the player.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param color: Color of the player's trail
        """
        # TODO: Set initial position, color, direction (e.g., [1, 0] for right)
        # Initialize an empty list for the player's trail
        self.x = x 
        self.y = y
        self.color = (255, 0, 0)
        self.direction = [1,0]
        self.trail = []
    
    def move(self):
        """
        Move the player based on their current direction.
        """
        # TODO: Update the player's position based on their direction
        # Add the new position to the trail
        self.x, self.y = self.x + self.direction[0], self.y + self.direction[1]
        self.trail.append([self.x, self.y])
    
    def change_direction(self, direction):
        """
        Change the player's direction.
        :param direction: New direction as a list [dx, dy]
        """
        # TODO: Update the player's direction
        # Ensure the new direction is not opposite to the current direction
        self.direction = self.direction if (direction[0] == -self.direction[0] or direction[1] == -self.direction[1]) else direction 

    def draw(self, screen):
        """
        Draw the player and their trail on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Draw the player's current position and their entire trail
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 1, 1))
        for i in self.trail: 
            pygame.draw.circle(screen, (255, 0, 0), (i[0], i[1], 1,1))
