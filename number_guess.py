#!/bin/bash/
# Created By W.H.Tharusha Rasanjana
# All Rights Reserved

import secrets
import random
import string
import sys

def generate(numbers):
	ilevel = 16 # adjust as you needed, but make sure that when this rises the computational feasibility to bring on loops go downs also!
	flevel = []
	ns = ""
	for i in range(ilevel**2): # replace the constant as you desired!
		flevel.append("".join(secrets.choice(numbers)))
	random.shuffle(flevel)
	for k in flevel:
		ns += k
	return "".join(secrets.choice(ns))


def main():
	tries = 0
	while True:
		marks = 100 - tries
		if tries >= 100:
			marks = 0
		usr = str(input("[INFO] Guess the number(0-9)['q' to quit]': "))
		if usr != '' and len(usr) == 1 and (usr in string.digits or usr == 'q'):
			if usr == 'q':
				print(f"[INFO] Thank you for playing with me, hope you've enjoyed!")
				sys.exit()
			gen = generate(string.digits)
			if usr == gen:
				print(f"[INFO] Your guess: {usr}, My guess: {gen},You won => your score {marks}!")
				return False
			else:
				print(f"[INFO] Your guess: {usr}, My guess: {gen},You lose, Try again!")
				tries += 1
		else:
			if usr == '':
				print("[ERROR] No input entered!")
				sys.exit()
			elif len(usr) != 1:
				print("[ERROR] Invalid numerical sequence!")
			elif usr not in string.digits or usr != 'q':
				print("[ERROR] Invalid input, your input is not valid!")
				sys.exit()
			else:
				print("[ERROR] An unknown error occured!")
				sys.exit()


if __name__ == '__main__':
	main()