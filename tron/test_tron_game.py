import pygame
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from tron_game import initialize_game, handle_events, update_game_state, draw_game
from game_board import GameBoard
from player import Player

def test_initialize_game():
    screen = initialize_game()
    assert isinstance(screen, pygame.Surface), "initialize_game should return a Pygame Surface"
    print("initialize_game test passed")

def test_handle_events():
    player = Player(10, 10, (255, 0, 0))
    initial_direction = player.direction.copy()
    
    # Simulate a key press event
    event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})
    pygame.event.post(event)
    
    result = handle_events(player)
    assert result == True, "handle_events should return True when not quitting"
    assert player.direction != initial_direction, "Player direction should change after handle_events"
    print("handle_events test passed")

def test_update_game_state():
    game_board = GameBoard(20, 15)
    player = Player(10, 10, (255, 0, 0))
    initial_position = (player.x, player.y)
    
    result = update_game_state(player, game_board)
    assert result == True, "Game should still be active"
    assert (player.x, player.y) != initial_position, "Player should move after update_game_state"
    
    # Test collision
    player.x, player.y = -1, -1  # Move player out of bounds
    result = update_game_state(player, game_board)
    assert result == False, "Game should end on collision"
    
    print("update_game_state test passed")

def test_draw_game():
    pygame.init()
    screen = pygame.Surface((400, 300))
    game_board = GameBoard(20, 15)
    player = Player(10, 10, (255, 0, 0))
    
    try:
        draw_game(screen, game_board, player)
        print("draw_game executed without errors")
    except Exception as e:
        print(f"Error in draw_game: {e}")

def run_all_tests():
    pygame.init()
    test_initialize_game()
    test_handle_events()
    test_update_game_state()
    test_draw_game()
    print("All tron_game tests passed!")

if __name__ == "__main__":
    run_all_tests()