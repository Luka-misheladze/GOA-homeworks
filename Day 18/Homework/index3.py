# მომხმარებელს ჰკითხეთ თავისი ასაკი და სახელი, 
# შემდეგ თქვენი მიზანია მისი სახელი დაბეჭდოთ იმდენჯერ რამდენი წლისაც არის მომხმარებელი:

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

for i in range(1, age + 1):
    print(name)