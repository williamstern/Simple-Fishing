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
            time.sleep(1)
            endTime = time.time() + (4 * 60)

   
    def random_fish(self):
        '''Randomly selects a type of fish and gives a point value'''
        # Here are some fish with point value
        fish = {"Bluegill": 12,
                "Largemouth Bass": 16,
                "Smallmouth Bass": 14,
                "Tuna": 25,
                "Minno": 0,
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
    
    def chance_of_catch(self, fish_value):
        time.sleep(2)
        # Makes the value positive and then makes it 4 times more likely
        chance = random.randomint(0, (abs(fish_value) // 4))
        if chance == 0: # Caught
            return True
        else: # Not 
            time.sleep(4)
            return False
            
    def catching(self):
        canCast = True
        while canCast = True:
            input("Press Enter to cast!")
                time.sleep(random.randomint(1,15))
                if self.chance_of_catch == True:
                    reeling = input("Quick! Press Enter to reel the fish in!")
                    if reeling == None:
                        print("Oh No! It got away!"
                        time.sleep(1)
                    else:
                        print("You cought a", random_fish_data[0], "worth", random_fish_data[1], "points.")
                        time.sleep(1.4)
            if time.time() >= endtime:
                canCast = False
                print("Your final score is", sum(fish.values()))
                time.sleep(5)
            
        
endtime = 0        
random_fish_data = []
foo = Fishing()
foo.setup()

