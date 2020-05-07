import data
import pandas as pd
from bs4 import BeautifulSoup
import html5lib
from urllib.request import urlopen
from bs4 import BeautifulSoup

#start at 2015 after hornets name change
teams_short_form = {'Cleveland Cavaliers':      'CLE',
                    'Detroit Pistons':          'DET',
                    'Dallas Mavericks':         'DAL',
                    'Memphis Grizzlies':        'MEM',
                    'Washington Wizards':       'WAS',
                    'Orlando Magic':            'ORL',
                    'Toronto Raptors':          'TOR',
                    'Chicago Bulls':            'CHI',
                    'Milwaukee Bucks':          'MIL',
                    'Boston Celtics':           'BOS',
                    'Miami Heat':               'MIA',
                    'Minnesota Timberwolves':   'MIN',
                    'Atlanta Hawks':            'ATL',
                    'Indiana Pacers':           'IND',
                    'Golden State Warriors':    'GSW',
                    'New Orleans Pelicans':     'NOP',
                    'Denver Nuggets':           'DEN',
                    'New York Knicks':          'NYK',
                    'Houston Rockets':          'HOU',
                    'Los Angeles Lakers':       'LAL',
                    'Los Angeles Clippers':     'LAC',
                    'Philadelphia 76ers':       'PHI',
                    'Sacramento Kings':         'SAC',
                    'San Antonio Spurs':        'SAS',
                    'Portland Trail Blazers':   'POR',
                    'Brooklyn Nets':            'BRK',
                    'Oklahoma City Thunder':    'OKC',
                    'Utah Jazz':                'UTA',
                    'Charlotte Hornets':        'CHO',
                    'Phoenix Suns':             'PHO'}

#year month day 0