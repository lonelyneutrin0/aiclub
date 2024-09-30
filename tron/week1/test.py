import pygame
import gym
import stable_baselines3

"""
This file will test your environment to ensure everything is set up correctly.
"""

def test_environment():
    tests_passed = 0
    total_tests = 3

    # Test 1: Check if Pygame is installed and can be initialized
    try:
        pygame.init()
        print("Test 1 passed: Pygame is installed and initialized successfully.")
        tests_passed += 1
    except:
        print("Test 1 failed: There was an error initializing Pygame.")

    # Test 2: Check if a Pygame window can be created
    try:
        screen = pygame.display.set_mode((100, 100))
        pygame.display.quit()
        print("Test 2 passed: Pygame window created successfully.")
        tests_passed += 1
    except:
        print("Test 2 failed: There was an error creating a Pygame window.")

    # Test 3: Check if OpenAI Gym and Stable-Baselines3 are installed
    try:
        gym.make("CartPole-v1")
        stable_baselines3.PPO
        print("Test 3 passed: OpenAI Gym and Stable-Baselines3 are installed.")
        tests_passed += 1
    except:
        print("Test 3 failed: There was an error with OpenAI Gym or Stable-Baselines3.")

    # Print final results
    print(f"\nTests passed: {tests_passed}/{total_tests}")
    if tests_passed == total_tests:
        print("All tests passed! Your environment is set up correctly.")
    else:
        print("Some tests failed. Please review the output and fix any issues.")

if __name__ == "__main__":
    test_environment()