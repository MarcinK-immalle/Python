class Lab:
    myIDs=[]
    myStudents=[]
    credits=[]

class Student:
    def __init__(self,studentName,studentID):
        self.name = studentName
        self.id = studentID
        self.credits = 0

    def getLogin(self):
        print(self.name[0:4] + self.id[0:3])

    def printStudent(self):
        print("Name: "+self.name + " ," + "Id: "+self.id + " ," + "credits: " + self.credits)

    def changeName(self, newName):
        self.name = newName
    
    def addCredits(self, addPoints):
        self.credits += addPoints

    