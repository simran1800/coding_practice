from bs4 import BeautifulSoup
import requests

n=int(input("Enter number of words to be searched:\n"))
for i in range(n):

	inp=input("Enter the word to be searched:\n")
	web = requests.get('https://www.lexico.com/definition/'+inp)

	data = web.content

	soup = BeautifulSoup(data,features="html.parser")

	tag = soup.find_all("span", "ind")

	if tag==[]:
		print("Enter valid word")

	a = 1
	for i in tag:
		print(str(a) + ". " + i.text)
		a = a + 1
		if a==5:
			break
	print("\n")


