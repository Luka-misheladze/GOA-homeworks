# 9)ფუნქცია რომელსაც გადაეცემა რიცხვი და აბრუნებს ამ რიცხვს მინუს ნიშნით , ანუ უარყოფითს

def negative_number(number):
    if number < 0:
        return number
    return -number

print(negative_number(-15))