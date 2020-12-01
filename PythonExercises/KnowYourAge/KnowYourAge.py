print("Find out when you will turn 100!!")
age_year=str(input("Enter your age or the year you were born"))
if len(age_year)>0 and len(age_year)<3:
    year_born = int(2020 - int(age_year))
    # res=100-int(age_year)
    print(f"you will turn 100 in the year {year_born+100}\n*********")
    op=input(f"Do you wish to know your age in any year ahead?(y/n)")
    if op=="y":
        n=int(input("Enter the year in which who want to know your age:"))
        year_born=int(2020-int(age_year))
        res=n-year_born
        print(f"You will be {res} years old in the year {n}")
    else:
        exit()


elif len(age_year)==3:
    print(f"you seem to be {age_year} years old. You are the oldest person alive ")



elif len(age_year)==4:
    if int(age_year)<2020:
        res=int(age_year)+100
        print(f"you will turn 100 in the year {res}\n**************")
        op = input(f"Do you wish to know your age in any year ahead?(y/n)")
        if op == "y":
            n = int(input("Enter the year in which who want to know your age:"))
            res = n - int(age_year)
            print(f"You will be {res} years old in the year {n}")
        else:
            exit()

    else:
        print("You are not yet born baby!")



