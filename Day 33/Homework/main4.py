# 4) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ პარამეტრს და დააჯამებს ყველა რიცხვს გარკვეულ შუალედში. მაგალითად შეკრიბავს რიცხვებს 5-დან 100-მდე.

def countrange(num, num1):
    result = 0
    for i in range(num, num1 + 1):
        result += i
    return result

print(countrange(1, 10))