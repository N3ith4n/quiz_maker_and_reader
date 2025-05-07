#imports
import os
import time
from math import floor
import random
import colorama

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
    
    questions = []
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if len(lines) != 6:
            print(f"Skipping malformed block (expected 6 lines, got {len(lines)}):\n{block}")
            continue

        try:
            question_text = lines[0].replace("Question: ", "").strip()
            choices = {}
            for line in lines[1:5]:
                if len(line) >= 3 and line[1] == ')':
                    choices[line[0].lower()] = line[3:].strip()
			
            correct = lines[5].replace("Correct answer: ", "").strip().lower()
            if correct in choices:
                questions.append({ 
                    "question": question_text,
                    "choices": choices,
                    "correct": correct
                })
            else:
                print(f"Skipping block (invalid correct answer '{correct}'):\n{block}")
        except Exception as e:
            print(f"Error parsing block:\n{block}\nError: {e}")
    
    return questions
 
#def function that will run the quiz stored
def run_quiz(filename):
    animated_center("Loading Quiz...")
    questions = load_questions(filename)

    if not questions:
        spec_print("\033[31mNo questions found in the quiz file.\033[39m\n")
        return

    spec_print(f"\033[32mLoaded {len(questions)} questions.\033[39m\n")
	
    random.shuffle(questions)
    score = 0

    for question_data in questions:
        spec_print("\033[36m" + question_data["question"] + "\033[39m", new_list=True)

        for letter, answer in question_data["choices"].items(): 
            spec_print(f"\033[33m{letter}. {answer}\033[39m", new_list=True)

        user_answer = input("\033[34mYour answer: ").lower()

        if user_answer == question_data["correct"]:
            spec_print("\033[32m✅ Correct!\033[39m\n")
            score += 1
        else:
            correct_choice = question_data["correct"]
            correct_answer = question_data["choices"][correct_choice]
            spec_print(f"\033[31m❌ Wrong.\033[39m The correct answer was {correct_choice}. {correct_answer}\n")

    spec_print(f"\033[32mYour final score: {score}/{len(questions)}\033[39m\n")

def ask_play_again():
    spec_print("\033[96mDo you want to play again? (y/n): ", new_list=False)
    answer = input().strip().lower()
    print("\033[39m", end="")
    return answer == "y"

#run the program
if __name__ == "__main__":
     while True:
        run_quiz("quiz.txt")
        if not ask_play_again():
            break
