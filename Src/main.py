import time

import Internals
import pygame
import sys

# Returns True when the run function exits its while True loop, this makes it so multiple screen can be used in the game
Done = Internals.App((800, 800)).Run()

pygame.quit()
time.sleep(3)
sys.exit()
