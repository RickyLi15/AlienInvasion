class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's static settings"""
      # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        
        # number of ships allowed
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10
       
        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # How quickly the alien point values increase
        self.score_scale = 1.5

       
        self.initialize_dynamic_settings()
      

    def initialize_dynamic_settings(self):
      """Initialize settings that change throughout the game."""
      # speed for the ship
      self.ship_speed = 6.0
      # speed for bullet
      self.bullet_speed = 5.0
      # speed for alein
      self.alien_speed = 4.0
       # fleet_direction of 1 represents right: -1 represents left
      self.fleet_direction = 1

       # How much points a player gets each time he/she shoot down an alien
      self.alien_points = 15



    def increase_speed(self):
       """Increase speed settings and alien point values"""
       self.ship_speed  *= self.speedup_scale
       self.bullet_speed *= self.speedup_scale
       self.alien_speed *= self.speedup_scale
       self.alien_points = int(self.alien_points * self.score_scale)
      
      
