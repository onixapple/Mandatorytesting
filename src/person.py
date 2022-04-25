from re import match

from src.generator import Generator
from src.address import address

class person:
    def __init__(self):
        Initials = Generator.genFullNameAndGender()
        self.firstName = Initials['name']
        self.lastName = Initials['surname']
        self.gender = Initials['gender']
        self.birthdate = Generator.genBirthDate()
        self.cpr = Generator.genCPR(self.gender, self.birthdate)
        self.phone = Generator.genPhoneNumber()
        self.address = address()
        Generator.insertPersonInDb(self.firstName,self.lastName,self.gender,self.birthdate,str(self.cpr),self.phone,self.address.street)
    #Debug
    def printPerson(self):
        print(f'First Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender} \nBirthdate: {self.birthdate} \nCPR: {self.cpr}')
        #Address
        print(f'Town: {self.address.town} \nZip Code: {self.address.zipCode} \nStreet Name and Number: {self.address.street} {self.address.number} \nFloor: {self.address.floor} \nDoor: {self.address.door}')
        Generator.insertPersonInDb(self.firstName, self.lastName, self.gender, self.birthdate, str(self.cpr),
                                   self.phone, self.address.street)
        print("Person added to database")
    def printCpr(self):
        print(f'CPR: {self.cpr}')

    def printFullNameAndGender(self):
        print(f'First Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender}')

    def printFullNameGenderBirth(self):
        print(f'First Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender} \nBirthdate: {self.birthdate}')

    def printCPRNameGender(self):
        print(f'CPR: {self.cpr} \nFirst Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender}')

    def printprintCPRNameGenderBirth(self):
        print(f'CPR: {self.cpr} \nFirst Name: {self.firstName} \nLast Name: {self.lastName} \nGender: {self.gender} \nBirthdate: {self.birthdate}')

    def printAdress(self):
        print(f'Town: {self.address.town} \nZip Code: {self.address.zipCode} \nStreet Name and Number: {self.address.street} {self.address.number} \nFloor: {self.address.floor} \nDoor: {self.address.door}')

    def printPhone(self):
        print(f'Phone: {self.phone}')

    def printMany(self,number):
        i = 0
        print('Generating New Person \n \n')
        while i < int(number):
            print('Generating New Person \n ')
            newperson = person()
            newperson.printPerson()
            i += 1
            print('')





