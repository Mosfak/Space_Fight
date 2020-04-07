class Settings():

    def __init__(self):

        #screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        #ship Settings
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 171, 0, 0
        self.bullets_allowed = 10
        self.bullets_limited = False

        