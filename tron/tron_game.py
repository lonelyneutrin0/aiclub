import pygame
from player import Player
from game_board import GameBoard
def initialize_game():
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    # TODO: Initialize Pygame
    # Create and return a Pygame screen object
    pygame.init()
    return pygame.display.set_mode((200, 200))


def handle_events(player:Player):
    """
    Handle Pygame events, including player input.
    :param player: Player object to update based on input
    :return: False if the game should quit, True otherwise
    """
    # TODO: Loop through Pygame events
    # Handle QUIT event
    # Handle KEYDOWN events to change player direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            return False
        if event.type==pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                player.change_direction([-1, 0])
                return True
            elif event.key == pygame.K_RIGHT:
                player.change_direction([1, 0])
                return True
            elif event.key == pygame.K_UP:
                player.change_direction([0, 1])
                return True
            elif event.key == pygame.K_DOWN:
                player.change_direction([0, -1])
                return True
        else: 
            return True

def update_game_state(player: Player, game_board: GameBoard):
    """
    Update the game state, including player movement and collision detection.
    :param player: Player object to update
    :param game_board: GameBoard object to check collisions against
    :return: False if the game is over (collision), True otherwise
    """
    # TODO: Move the player
    player.move()
    # Check for collisions with game_board
    if game_board.is_collision(player.x, player.y): return False 
    
    # Update game_board with new player position
    game_board.grid = player.trail
    


def draw_game(screen, game_board: GameBoard, player: Player):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player: Player object to draw
    """
    # TODO: Clear the screen
    screen.fill(0, 0,0)
    # Draw the game board
    game_board.draw(screen)
    # Draw the player
    player.draw(screen)
    # Update the display
    screen.display.flip()

def main():
    """
    Main game loop.
    """
    # TODO: Initialize the game
    screen = initialize_game()
    # Create game objects (game_board, player)
    game_board = GameBoard(800, 600)
    player = Player(100, 100, (255,0,0))
    running = True
    clock = pygame.time.Clock
    # Run the game loop:
    while running == True: 
    #   - Handle events
        running = handle_events()
    #   - Update game state
        update_game_state()
    #   - Draw game
        draw_game()
    #   - Control game speed
        clock.Tick(60)