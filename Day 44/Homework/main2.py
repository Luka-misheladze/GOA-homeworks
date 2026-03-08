# 4) დაწერეთ ფუნქცია სახელად sumDigits
# რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მისი ციფრების ჯამს.

def sumDigits(number):
    summed = 0
    for i in str(number):
        summed = summed + int(i)
    return summed

print(sumDigits("69"))