import random

print("Snake Water Gun")
print("A game of 3 rounds starts....\n")
user_score = 0
comp_score = 0

play=["snake","water","gun"]
n=[1,2,3]


def check(comp, user):
	if comp==user:
		return "**Its a Tie**"
	elif comp==2 and user==1:
		return "**You Win**"
	elif comp==3 and user==2:
		return "**You Win**"
	elif comp==1 and user==3:
		return "**You Win**"
	elif comp==3 and user==1:
		return "**You Lose**"
	elif comp==2 and user==3:
		return "**You Lose**"
	elif comp==1 and user==2:
		return "**You Lose**"
	else:
		return "Enter Valid Option"

for i in range(3):
	comp = random.choice(n)
	user = int(input("enter your choice in digits:\n1=>Snake\n2=>Water\n3=>Gun\n"))
	print("Your play:", play[user - 1])
	print("Opponent's play:", play[comp - 1])
	res=check(comp,user)
	print(res)
	if res=="**You Win**":
		user_score+=1
	elif res=="**You Lose**":
		comp_score+=1
	print("Your Score:",user_score)
	print("Opponent's Score:",comp_score)
	print()

print("****FINAL SCORES****")
print("You ended up with: "+str(user_score)+" score")
print("Opponent ended up with: "+str(comp_score)+" score")
print()


if user_score>comp_score:
	print("*******YOU ARE THE WINNER********")
elif user_score<comp_score:
	print("*******YOU LOST THE GAME.BETTER LUCK NEXT TIME********")
else:
	print("*******ITS A TIE.PLAY AGAIN********")




