# მომხმარებელს შემოატანინეთ რიცხვი მანამ სანამ ესრიცხვი არ იქნება ლუწი,
# ხოლო როდესაც მომხმარებელი შეიყვანს ლუწ რიცხვს , ტერმინალში დაიპრინტოს
# "You enter an even number and the loop is over"

number = int(input("Please enter a number: "))

while number % 2 != 0:
    number = int(input("Please enter a number: "))

print("you entered an even number")