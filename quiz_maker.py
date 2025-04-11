#imports for another function
import os
import time
from math import floor

#make a function that adds a delay before printing each character
def spec_print(text, speed=0.03, new_list=False):
	for character in text:
		print(character, end="", flush=True)
		time.sleep(speed)
	if(new_list):
 		print("") 

#make a function that produces a loading animation at the start
def animated_center(text):
	#functions that will get the terminal size and setup the necessary animation variables
	center = os.get_terminal_size().columns
	arrows = 1
	duration = 6
	max_arrows = 3

	#another terminal clearer
	print("\033[H\033[J", end="")

	#main animation loop (while loop)
	while duration > 0:
		space = floor(center / 2) - (floor(len(text) / 2) + 1 + max_arrows)
		spacer = " " * space

		#functions for the animation of arrows going to the center (appearing)
		print(spacer + f"{('>' * arrows) + ' ' * (max_arrows - arrows)} {text} {' ' * (max_arrows - arrows) + ('<' * arrows)}" + spacer, end="\033[H", flush=True)
		time.sleep(0.1)
		duration -= 0.1
		arrows += 1

		#if loop for the animation that makes the arrows disappear
		if arrows > max_arrows:
			spaces_that_eats_the_arrows = 0
			arrows = max_arrows

			time.sleep(0.3)
			duration -= 0.3
			
			while arrows != 0: 
				spaces_that_eats_the_arrows += 1
				arrows -= 1
				print(spacer + f"{(' ' * spaces_that_eats_the_arrows) + '>' * arrows} {text} {'<' * arrows + ' ' * spaces_that_eats_the_arrows}" + spacer, end="\033[H", flush=True)
				time.sleep(0.1)
				duration -= 0.1

			time.sleep(0.3)
			duration -= 0.3
			
	#clears the terminal once the animation has finished
	print("\033[H\033[J", end="")
  
#make a function
def create_quiz(filename):
	animated_center("loading...")
	with open(filename, "a") as f:
		choices = ["a", "b", "c", "d"]
		while True:
			spec_print('Enter a question (type "stop" to finish): ')
			question = input()
			if question.lower() == "stop":
				break

			answers = {}
			correct = ""
			for choice in choices:
				spec_print(f"{choice}. ")
				ans = input()
				spec_print("Is this the correct answer? (y/n): ")
				is_correct = input().lower()
				answers[choice] = ans
				if is_correct == "y":
					correct = choice

			#animated file-writing style print
			index = 0 
			while index < len(question):
				print(f"{filename} < {question[index:]}")
				index += 1
				time.sleep(0.1)

			#write to file
			f.write(f"Question: {question}\n")
			for key in choices:
				f.write(f"{key}) {answers[key]}\n")
			f.write(f"Correct answer: {correct}\n\n")

#run
create_quiz("quiz.txt")
