class Lab:
    def __init__(self, maxStudents):
        self.teacher = "unknown"
        self.room = "unknown"
        self.timeAndDay = "unknown"
        self.students = students[]
        self.capacity = maxStudents
    
    def enrollStudent(self, newStudent):
        if(self.capacity == maxStudents) {print("The class is full, you cannot enrol.")}
        else{students.add(newStudent);}
    
    def numberOfStudents(self):
        return students.size();
    
    def setRoom(self,roomNumber):
        self.room = roomNumber;
    
    def setTime(self,timeAndDaySting):
        selftimeAndDay = timeAndDaySting;

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

    if __name__ == '__main__':
        student1 = student(joske,123456);
        printStudent(student1)