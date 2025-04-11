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
