import pandas as pd
import game
import box_score

class Team:
    def __init__(self, name):
        self.name = name
        self.games = []

    def addgame(self, name, home, away,
                pts_home, pts_away, home_box, away_box):
        self.games.append(game.game(name, home, away, pts_home, pts_away, home_box, away_box))