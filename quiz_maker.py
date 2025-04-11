#imports for another function
import os
import time
from math import floor

#make a function that produces a loading animation at the start
def animatedCenter(text):
  #functions that will get the terminal size and setup the necessary animation variables
  c = os.get_terminal_size().columns #gets the width of the terminal so the animation will be placed in the center
	n = 1 #starting animation counter (the arrows will start at 1 then up to the number of maxn)
	duration = 6 #the animation will run for 6 seconds
	maxn = 3 #how wide the arrows should stretch before disappearing the same way

  #main animation loop (while loop)

  #clears the terminal once thr animation has finished

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
