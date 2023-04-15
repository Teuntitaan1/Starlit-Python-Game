import Internals
import pygame
import sys

# Returns True when the run function exits its while True loop, this makes it so multiple screen can be used in the game
Done = Internals.App((1000, 800)).Run()

pygame.quit()
sys.exit()