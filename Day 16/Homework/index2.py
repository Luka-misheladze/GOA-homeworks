# წავა თუ არა მომხმარებელი ჯარში?

age = int(input("please enter your age: "))
height = float(input("please enter your height: "))
weight = float(input("please enter your weight: "))

standart = age >= 18 and height > 170.5 and weight > 55.5

print("")
print(standart)


# ///////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////


# ეს შეიძლება მეორე ნაირადაც : 

print("")

user_age = int(input("please enter your age: "))
user_height = float(input("please enter your height: "))
user_weight = float(input("please enter your weight: "))

print("")

if user_age >= 18 and user_weight > 55.5 and user_height > 170.5:
    print("True")
else:
    print("False")