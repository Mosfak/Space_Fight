class Settings():

    def __init__(self):

        #screen Settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #ship Settings
        #self.ship_speed_factor = 3
        self.ship_limit = 2

        #Bullet Settings
        #self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 171, 0, 0
        self.bullets_allowed = 5
        self.bullets_limited = True

        #alien settings
        #self.alien_speed = 1
        self.alien_drop_speed = 1
        self.alien_direction = -1

        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 5
        self.alien_speed = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        