import json
class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        # Reads the high score from a file when the game opens
        try:
            with open('highscore.txt') as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
                self.high_score = 0
                
           

        
        # start alien invasion in an inactive state
        self.game_active = False
    def reset_stats(self):

        """Initialize statistics that can change during game. """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
