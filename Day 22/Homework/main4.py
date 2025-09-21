# მომხმარებელს შემოატანინეთ რიცხვი , თქვენი მიზანია გაიგოთ ეს რიცხვი დადებითია
# უარყოფითია თუ ნულის ტოლია.

number = float(input("Please enter a random number: "))

if number > 0:
    print("რიცხვი დადებითია")
elif number < 0:
    print("რიცხვი უარყოფითია")
else:
    print("რიცხვი არის ნულის ტოლი")