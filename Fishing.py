# William Stern
# 05.02.2017

import time 
import random

class Fishing(object):
    
    def __init__(self):
        self.highscores = {}
        self.fishinglog = {}
        
    def setup(self):
        ''' This makes for an easy setup'''
        # A print of a pond
        print('|    1    |    2    |    3    |')
        print('-------------------------------')
        print('|    4    |    5    |    6    |')
        print('-------------------------------')
        print('|    7    |    8    |    9    |')
        print('')
        print("Hello! Welcome to Fishing!", end = '\r')
        time.sleep(3)
        print('                                       ', end = "\r")
        # Note: add instructions here
        ready = input('Are you ready? [Y/N] ')
        if ready == 'n' or ready =='N':
            exit()
        else:
            # Countdown
            print('3', end = '\r')
            time.sleep(1)
            print('2', end = '\r')
            time.sleep(1)
            print('1', end = '\r')
            time.sleep(1)
            print('GO!', end = '\r')

   
    def random_fish(self):
        '''Randomly selects a type of fish and gives a point value'''
        # Here are some fish with point value
        fish = {"Bluegill": 2,
                "Largemouth Bass": 5,
                "Smallmouth Bass": 4,
                "Tuna": 25,
                "Minno": 1,
                "Lionfish": -25,
                "Gar": 26,
                "Electric Eel": -28}

        # Gets a random sample of a fish which is then turned into a list
        # Then the list gets turned into a string
        random_fish_key = ''.join(random.sample(list(fish),1))
        # Uses random_fish_key to get a value out of fish
        random_fish_value = fish.get(random_fish_key)
        # Puts them together in a list
        random_fish_data = [random_fish_key, random_fish_value]
        # Adds the fish key and value to the log
        self.fishinglog.update({random_fish_key: random_fish_value})
        
        return random_fish_data
        
foo = Fishing()
foo.setup()

