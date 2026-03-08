# 6) დაწერეთ ფუნქცია, რომელიც მიიღებს ორ პარამეტრს
# და დააჯამებს ყველა რიცხვს გარკვეულ შუალედში.
# მაგალითად შეკრიბავს რიცხვებს 5-დან 100-მდე.

def count(start, end):
    summed = 0
    for i in range(start, end + 1):
        summed = summed + i
    return summed

print(count(1,3))