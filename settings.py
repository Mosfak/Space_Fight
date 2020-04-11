class Settings():

    def __init__(self):

        #screen Settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #ship Settings
        self.ship_speed_factor = 3
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed_factor = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 171, 0, 0
        self.bullets_allowed = 10
        self.bullets_limited = False

        #alien settings
        self.alien_speed = 1
        self.alien_drop_speed = 1
        self.alien_direction = -1

        #score handling