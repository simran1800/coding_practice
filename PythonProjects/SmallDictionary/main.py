import json
data=json.load(open("data.json"))

def dictionary(word):
    if word in data:
        return data[word]
    else:
        return "Not found"

n=int(input("Enter number of words to be searched: "))
for i in range(n):
    user=input("Enter the word to be searched: ")
    result=dictionary(user)

    if type(result)==list:
        for i in result:
            print(i)
    else:
        print(result)