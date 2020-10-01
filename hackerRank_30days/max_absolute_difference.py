#Complete the Difference class by writing the following:

#A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
#A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the maximumDifference instance variable.


****************************************************************
class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):

        self.maximumDifference=abs(max(self.__elements)-min(self.__elements))
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

**************************************************************************
#naive method:


class Difference:
    # def __init__(self, a):
    #     self.__elements = a

    # Add your code here
    def __init__(self,a):
        self.elements=a

    def computeDifference(self):
        self.list=[]
        for i in range(0,_):      #select one item from list
            x=self.elements[i]
            p=i+1
            for j in range(p,_):  #select the rest of the elements after the previous selected
                y=self.elements[j]
                diff=x-y
                q=abs(diff)
                print(x , "-" , y , "=",q)
                self.list.append(q)
        self.maximumDifference=max(self.list)
        print("Maximum:",self.maximumDifference)

                #print(abs(diff))



# End of Difference class

_ = int(input())
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

# print(d.maximumDifference)