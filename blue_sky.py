import pygame

from blue_settings import Blue_Settings
from bs_ship import Bs_Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    bs_settings = Blue_Settings()
    bs_screen = pygame.display.set_mode(
        (bs_settings.bs_screen_width, bs_settings.bs_screen_height))

    pygame.display.set_caption("Blue sky")

    # Make a ship.
    bs_ship = Bs_Ship(bs_screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        gf.update_bs_screen(bs_settings, bs_screen, bs_ship)



run_game()