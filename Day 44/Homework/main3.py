# 5) დაწერეთ ფუნქცია სახელად countBs
# რომელიც იღებს სტრიქონს თავის ერთადერთ არგუმენტად
# და აბრუნებს სტრიქონში დიდი "B" სიმბოლოების რაოდენობას.

def countBs(sentence):
    count = 0
    for i in sentence:
        if i == "B":
            count = count + 1
    return count

print(countBs("hello Bears.. i love my Beard and lets drink Beer together"))