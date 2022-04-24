import argparse

from person import person

parser = argparse.ArgumentParser(description = "Generates Fake information for non-existing danish persons")
parser.add_argument("--instances", type = int, default = 5, help = "How many data instances to generate, value = int")
parser.add_argument("--datatype", type = str, default = "person",
  choices=['cpr', 'namegender', 'namegenderbirthdate', 'cprnamegender', 'cprnamegenderbirthdate', 'address', 'phone', 'person'], help = "What to generate" )

def start():

  newPerson = person()

  print('1. Generate one random person\n'
        '2. Generate one random CPR\n'
        '3. Generate random Full Name and Gender\n'
        '4. Generate one random Full Name Gender and Birth\n' 
        '5. Generate one random CPR Name and Gender\n'
        '6. Generate one random Address\n'
        '7. Generate one random Phone number\n'
        '8. Generate many random users\n')
  userInput = input('What do you want to generate?')

  if userInput == "1":
      newPerson.printPerson()
      start()
  elif userInput == "2":
      newPerson.printCpr()
      start()
  elif userInput == "3":
      newPerson.printFullNameAndGender()
      start()
  elif userInput == "4":
      newPerson.printprintCPRNameGenderBirth()
      start()
  elif userInput == "5":
      newPerson.printCPRNameGender()
      start()
  elif userInput == "6":
      newPerson.printAdress()
      start()
  elif userInput == "7":
      newPerson.printPhone()
      start()
  elif userInput == "8":
      number = input('How many you want to generate?')
      newPerson.printMany(number)
      start()

start()
#switch nr of persons
