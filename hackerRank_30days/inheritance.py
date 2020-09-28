
###### Task:You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
# Completed code for Person and a declaration for Student are provided for you in the editor.
# Observe that Student inherits all the properties of Person.






class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    sum=0

    def __init__(self, firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores=scores

    def calculate(self):
        
        for item in self.scores:
            self.sum+=item
        self.avg=self.sum/len(self.scores)
        

        if self.avg>=90 and self.avg<=100:
            return "O"
        elif self.avg>=80 and self.avg<90:
            return "E"
        elif self.avg>=70 and self.avg<80:
            return "A"
        elif self.avg>55 and self.avg<70:
            return "P"
        elif self.avg>=40 and self.avg<55:
            return "D"
        else:
            return "T"



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
# print(s.firstName,s.lastName,s.idNumber,s.scores)
s.printPerson()
print("Grade:", s.calculate())