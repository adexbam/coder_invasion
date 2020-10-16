import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible.
        pygame.display.flip()


def update_bs_screen(bs_settings, bs_screen, bs_ship):
        # Redraw the screen during each pass through the loop.
        bs_screen.fill(bs_settings.bg_color)
        bs_ship.blitme()

        # make the most recently drawn screen visible.
        pygame.display.flip()