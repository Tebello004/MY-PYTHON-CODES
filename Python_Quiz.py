# This my python quiz most of the question are based on python programming language.

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "Central processing unit":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("Which type of programming does python support? ")
if answer.lower() == "Object oriented programming":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What does OOP stand for? ")
if answer.lower() == "Object oriented programming":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What does SDK stand for? ")
if answer.lower() == "Software development kit":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("Is python case sensitive when dealing with identifiers? ")
if answer.lower() == "yes":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What is the correct extension of python file? ")
if answer.lower() == ".py":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("Is python code compiled or interpreted? ")
if answer.lower() == "both":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("All keywords in python are in lower case (True or false) ")
if answer.lower() == "false":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("Which keyword is  used for function in python language? ")
if answer.lower() == "def":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What does PIP stand for? ")
if answer.lower() == "Preferred installer program":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("Python supports the creation of anonymous function at runtime, using a construct called? ")
if answer.lower() == "lambda":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What does SSL stand for? ")
if answer.lower() == "Secure sockets layer":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What does URL stand for? ")
if answer.lower() == "Uniform resource locator":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')

answer = input("What is the full name of management referred to as Git? ")
if answer.lower() == "None":
  print('Correct!')
  score += 1
else:
  print('Incorrect try again')
  
print("You got " + str(score) + " questions correct!!")
print("You got " + str((score / 14) * 100) + " %.")