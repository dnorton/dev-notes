# Monty Hall Problem
# Copied and modified from the original
# by James Tauber
# http://jtauber.com/
# Original: http://jtauber.com/2007/06/monty_hall.py

import random

DOORS = [1, 2, 3]

class Game:

	 def __init__(self, game_count):
			self.stay_count = 0
			self.switch_count = 0

			for count in range(1, game_count + 1):
				 self.go()

			print "stay = %s%%, switch = %s%%, count=%s" % (100 * self.stay_count / game_count, 100 * self.switch_count / game_count, game_count)

	 def go(self):

			car_behind = random.choice(DOORS)
			first_choice = random.choice(DOORS)
			monty_opens = random.choice([door for door in DOORS if door != car_behind and door != first_choice])

			# print "car is placed behind door", car_behind
			# print "contestant chooses door", first_choice
			# print "monty opens door", monty_opens

			stayer = first_choice
			switcher = [door for door in DOORS if door != monty_opens and door != first_choice][0]

			# print "stayer would stick with door", stayer
			# print "switcher would change to door", switcher

			if car_behind == stayer:
				 # print "stayer would win"
				 self.stay_count += 1
			elif car_behind == switcher:
				 # print "switcher would win"
				 self.switch_count += 1
			else:
				 print "neither would win"
				 return 0


Game(10000)
