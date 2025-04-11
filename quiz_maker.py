#imports for another function
import os
import time
from math import floor

#make a function that produces a loading animation at the start
def animatedCenter(text):
	#functions that will get the terminal size and setup the necessary animation variables
	center = os.get_terminal_size().columns
	arrows = 1
	duration = 6
	max_arrows = 3

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
			spaces_that_eats_the_arrows = 0 #initialize
			arrows = max_arrows #this prevents the amount of arrows from going over 3

			time.sleep(0.3) #another interval before the arrows are 'eaten' by spaces (like before the start of the eating happens)
			duration -= 0.3 #decreases the duration to ensure that the animation finsihes on time
			
			while arrows != 0: 
				spaces_that_eats_the_arrows += 1 #add a space
				arrows -= 1 #remove an arrow to simulate it getting 'eaten'
				#this is where the actual eating happens
				print(spacer + f"{(' ' * spaces_that_eats_the_arrows) + '>' * arrows} {text} {'<' * arrows + ' ' * spaces_that_eats_the_arrows}" + spacer, end="\033[H", flush=True)
				time.sleep(0.1) #this interval is the time before another arrow is eaten after the one before it
				duration -= 0.1 #decreases the duration to ensure that the animation finsihes on time

			time.sleep(0.3) #this is the interval before another cycle begins
			duration -= 0.3 #decreases the duration to ensure that the animation finsihes on time
			
	#clears the terminal once the animation has finished

  return True
  
#make a function
def createQuiz(filename):
  #open a file in append mode to avoid overwriting previous data
  with open(filename, "a") as f:
    choices = ["a", "b", "c", "d"]
    #while loop for inputting the questions and answers
    while True:
      question = input('Enter a question (type "stop" to finish): ')
      if question.lower() == "stop":
        break
        
      #empty dictionary to store the answers effecrively
      answers = {}
      correct = ""
      #for loop for inputting the answers
      for choice in choices:
        ans = input(f"{choice}. ")
        is_correct = input("Is this the correct answer? (y/n): ").lower()
        answers[choice] = ans
        if is_correct == "y":
          correct = choice

      #organizes the format of the txt
      f.write(f"Question: {question}\n")
      for key in choices:
        f.write(f"{key}) {answers[key]}\n")
      f.write(f"Correct answer: {correct}\n\n")

#run
createQuiz("quiz.txt")
