#input the details of your diet and exercise and it will we stored in a file and 
#later can be retrieved with the time at which the information was entered.



import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for exercise\nEnter 2 for food\n"))
        if(c==1):
            value=input("What do you want to add?\n")
            with open("employee-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully added")
        elif(c==2):
            value = input("What do you want to add?\n")
            with open("employee-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully added")
    elif(k==2):
        c = int(input("Enter 1 for exercise\nEnter 2 for food\n"))
        if (c == 1):
            value = input("What do you want to add?\n")
            with open("student-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully added")
        elif (c == 2):
            value = input("What do you want to add?\n")
            with open("student-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully added")

    else:
        print("Please enter valid input => 1(employee),2(student)\n")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for exercise\nEnter 2 for food\n"))
        if(c==1):
            with open("employee-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("employee-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for exercise\nEnter 2 for food\n"))
        if (c == 1):
            with open("student-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("student-food.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("Please enter valid input => 1(employee),2(student)\n")
print("Daily Records")
a=int(input("Press 1 to input the value\nPress 2 to retrieve "))

if a==1:
    b = int(input("press 1 for employee\nPress 2 for student"))
    take(b)
else:
    b = int(input("press 1 for employee\nPress 2 for student"))
    retrieve(b)