import sys

from table import *

class App:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((300, 430))
        Block.init_rotate()
        TRS(screen)

    def main(self):
        clock = pygame.time.Clock()  # Create game clock
        count = 1
        # Enter the game loop
        while True:
            # Set refresh frame rate
            clock.tick(15)

            # Incident detection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Exit event
                    sys.exit()

            if TRS.STATUS == 0:
                TRS.new_blk()
                if TRS.check_action(TRS.cbk.x, TRS.cbk.y, TRS.cbk.blk, TRS.cbk.angle):
                    TRS.STATUS = 1
                else:
                    TRS.STATUS = 3
                    print("GAME OVER")
            elif TRS.STATUS == 1:
                TRS.action(pygame.key.get_pressed())
                if count % 10 == 0:
                    TRS.check_drop()
            elif TRS.STATUS == 2:
                TRS.check_clear()
                TRS.STATUS = 0

            TRS.print_game()
            pygame.display.update()  # Refresh screen
            count += 1

App().main()