#make a function
def createQuiz(filename):
  #open a file in append mode to avoid overwriting previous data
  with open(filename, "a") as f:
    choices = ["a", "b", "c", "d"] #added the choices that will be used for the while loop
    #while loop for inputting the questions and answers
    while True:
      question = input('Enter a question (type "stop" to finish): ')
      if question.lower() == "stop": #lowers the input just to make sure it matches the required input I placed
        break #it breaks as it is for the stop function
        
      #empty dictionary to store the answers effecrively

      #for loop for inputting the answers

      #organizes the format of the txt

#run
createQuiz("test.txt")
