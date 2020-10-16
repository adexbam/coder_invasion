import pygame

class Bs_Ship():

    def __init__(self, bs_screen):
        """Initialize the ship and set its starting position."""
        self.bs_screen = bs_screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ufo.png')
        self.rect = self.image.get_rect()
        self.bs_screen_rect = bs_screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.bs_screen_rect.centerx
        self.rect.bottom = self.bs_screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.bs_screen.blit(self.image, self.rect)
