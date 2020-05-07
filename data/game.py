import pandas as pd
import box_score

class game:
    def __init__(self, name, home, away,
                pts_home, pts_away, home_box, away_box):
        self.name = name
        self.home = home
        self.away = away
        self.pts_home = pts_home
        self.pts_away = pts_away
        self.box_score = box_score.box_score(home_box, away_box)