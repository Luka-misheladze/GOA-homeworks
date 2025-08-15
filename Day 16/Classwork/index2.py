# მომხმარებელს ვკითხოთ ასაკი და გავიგოთ სრულწლოვანია თუ არა :

age = int(input("Please enter your age: "))

if age >= 36:
    print("you are too old")
elif age < 18:
    print("Your underage")
else:
    print("you are an adult!")

# //////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////


# ასეც შეიძლება (მარტივი გზით) :
# True - სრულწლოვანი , False - არასრულწლოვანი.

age = int(input("please enter your age: "))
print(age >= 18)