class Lab:
    def __init__(self, maxStudents):
        self.teacher = "unknown"
        self.room = "unknown"
        self.timeAndDay = "unknown"
        self.students = []
        self.capacity = maxStudents
    
    def enrollStudent(self, newStudent):
        if len(self.students) >= self.capacity:
            print("The class is full, you cannot enrol.")
        else: 
            self.students.append(newStudent)
    
    def numberOfStudents(self):
        return len(self.students)
    
    def setRoom(self,roomNumber):
        self.room = roomNumber
    
    def setTime(self,timeAndDaySting):
        self.timeAndDay = timeAndDaySting

class Student:
    def __init__(self,studentName,studentID):
        self.name = studentName
        self.id = studentID
        self.credits = 0

    def getLogin(self):
        print(self.name[0:4] + self.id[0:3])

    def printStudent(self):
        print("Name: {name}, Id: {id}, credits {credits}".format(name=self.name, id=self.id, credits=self.credits))

    def changeName(self, newName):
        self.name = newName
    
    def addCredits(self, addPoints):
        self.credits += addPoints

if __name__ == '__main__':
    student1 = Student("Druzel", "123456")
    student1.printStudent()
    student2 = Student("Mats","321321")
    student2.printStudent()
    student1.getLogin()
    student2.getLogin()
    lab1 = Lab(1)
    lab1.enrollStudent(student1)
    lab1.enrollStudent(student2)