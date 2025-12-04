# 3) დაწერეთ ფუნქცია სახელად countBs, რომელიც იღებს სტრიქონს თავის ერთადერთ არგუმენტად და აბრუნებს სტრიქონში დიდი "B" სიმბოლოების რაოდენობას.

def countBs(sentence):
    count = 0
    for i in sentence:
        if i == "B":
            count += 1
    return count

print(countBs("hello Bears, I love my Beard"))