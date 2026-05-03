# 1) დაწერე ფუნქცია is_adult რომელიც პარამეტრად მიიღებს ასაკს და დააბურნებს:
# "adult" თუ ასაკი >= 18  და "Minor" თუ ასაკი < 18ზე.

def is_adult(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")

is_adult(int(input("Please enter your age: ")))