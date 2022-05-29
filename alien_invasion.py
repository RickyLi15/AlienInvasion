import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources,"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")
        # sets the color for the game backgrounds
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # detects key presses and releases
            self._check_events()
            self.ship.update()
            self._update_bullets()
            # redraws the screen on each pass through the loop
            self._update_screen()

           
           
            
          

    def _check_events(self):

        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # if the right key is pressed down, the ship will move
            # to the right continuously, until the right key is released
            elif event.type == pygame.KEYDOWN:
              self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
             self.ship.moving_left = True
        # the game quits when the player presses Q
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self): 

        """Create a new bullet and add it to the bullets group."""

        # if the number of bullets fired has not exceeded the number
        # of bullets allowed, we will fire another bullet
        if (len(self.bullets) < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Updates the position of bullets and get rid
        of old bullets"""

        # updates bullet position
        self.bullets.update()

        # gets rid of bullets that have disappeared,if the position
        # of the bottom of the bullet has went beyond the top of the 
        # screen, we remove the bullet from the group
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):

        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
