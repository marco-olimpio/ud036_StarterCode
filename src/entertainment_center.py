"""
This module is responsible for all the load of the movies and call the module
fresh_tomatoes.
"""

import src.fresh_tomatoes
import src.media

GUARDIANS = src.media.Movie('Guardian of the Galaxy',
                            'A group of intergalactic criminals are forced to'
                            ' work together to stop a fanatical warrior '
                            'from taking control of the universe.',
                            'https://bit.ly/2Ci8OvL',
                            'https://youtu.be/d96cjJhvlMA?t=41')

SCHINDLERS = src.media.Movie('Schindler\'s List',
                             'In German-occupied Poland during World War II, '
                             'Oskar Schindler gradually becomes concerned for '
                             'his Jewish workforce after witnessing their '
                             'persecution by the Nazi Germans',
                             'https://bit.ly/2JLgbxH',
                             'https://www.youtube.com/watch?v=mxphAlJID9U')

MATRIX = src.media.Movie('Matrix',
                         'A computer hacker learns from mysterious rebels '
                         'about the true nature of his reality '
                         'and his role in the war against its controllers.',
                         'https://bit.ly/2T06fDK',
                         'https://www.youtube.com/watch?v=m8e-FF8MsqU')

PULP = src.media.Movie('Pulp Fiction',
                       'The lives of two mob hitmen, a boxer, a gangster\'s '
                       'wife, and a pair of diner bandits intertwine in four '
                       'tales of violence and redemption. ',
                       'https://bit.ly/2ShI8jZ',
                       'https://www.youtube.com/watch?v=s7EdQ4FqbhY')

SCARFACE = src.media.Movie('Scarface',
                           'In Miami in 1980, a determined Cuban immigrant '
                           'takes over a drug cartel and succumbs to greed. ',
                           'https://bit.ly/2PRhLQ5',
                           'https://youtu.be/7pQQHnqBa2E')

BLADE = src.media.Movie('Blade Runner',
                        'A blade runner must pursue and terminate four '
                        'replicants who stole a ship in space, and have '
                        'returned to Earth to find their creator.',
                        'https://bit.ly/2EG0U1m',
                        'https://youtu.be/eogpIG53Cis')

MOVIES = [GUARDIANS, SCHINDLERS, MATRIX, PULP, SCARFACE, BLADE]
src.fresh_tomatoes.open_movies_page(MOVIES)
