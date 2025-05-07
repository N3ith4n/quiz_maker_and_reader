#imports
import os
import time
from math import floor
import random

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

#def function that will read the txt file then store it in the program to be used for the program that will run the quiz
def load_questions(filename):
    with open(filename, "r") as file_reader:
        content = file_reader.read().replace('\r\n', '\n').strip()
        blocks = [b.strip() for b in content.split('\n\n') if b.strip()]
    
    questions = [] #empty list that will store the questions
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()] #this now splits the blocks into lines to determine which is the question, choices and answer
        if len(lines) != 6:  #checks that there are 6 lines per block and if there isnt, these guys below (a warning) runs and skips that block
            print(f"Skipping malformed block (expected 6 lines, got {len(lines)}):\n{block}")
            continue

        try:
            question_text = lines[0].replace("Question: ", "").strip() #this removes the word "Question: " so that when its printed in the terminal it will look fine
            choices = {} #this stores the questions
            for line in lines[1:5]:  #we know that question is in line 0 and answer in line 5 so we want the loop to start in line 1 and end in line 4
                if len(line) >= 3 and line[1] == ')': #this makes sure the format of the choices will be something like a) , b) , and so on
                    choices[line[0].lower()] = line[3:].strip() #lowers the letter in index 0 just to make sure its not A) but a) and removes the whitespaces in the actual choices so it's easier to store
								#then stores the choices in the empty dictionary we initialized earlier

#def function that will run the quiz stored

#run the program
