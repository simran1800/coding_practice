import requests

# Making a GET request
r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

with open("iris.txt","a") as f:
    f.write(r.text)

f=open("iris.txt")
l=f.readlines()
f.close()
# print(l)

import pickle

# pickling---storing the data
fileobj=open("iris.pkl","ab")
pickle.dump(l,fileobj)
fileobj.close()

#reading pickled file
fileobj=open("iris.pkl","rb")
myfile=pickle.load(fileobj)
print(myfile)
fileobj.close()