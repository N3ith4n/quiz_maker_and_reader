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
      correct = "" #added a variable that will store the correct letter (just for better organization)
      #for loop for inputting the answers
      for choice in choices:
        ans = input(f"{choice}. ") #the user will be asked to input the choices and will be asked if its the correct answer or not
        is_correct = input("Is this the correct answer? (y/n): ").lower() #lowers it just to match what the code needs
        answers[choice] = ans #inputs the answers to the dictionary, the choice letter will be the keyw
        if is_correct == "y": #if the user input 'y', the letter of that choice will be inputted to the variable "choice"
          correct = choice

      #organizes the format of the txt

#run
createQuiz("test.txt")
