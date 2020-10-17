class Settings():
    """A class to store all settings for alien invasion"""


    def __init__(self):
        """initialize the game's settings."""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 1.5