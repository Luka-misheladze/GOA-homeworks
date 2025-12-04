# 2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია და ამ სიას გაფილტრავს დაყოფს ორ ნაწილად დადებითებად და უარყოფითებად:

number_list = [1, 5, -34, -11, 92, -72, 84, 9, -46, -123, 3]
def positive_or_negative(number):
    positive = []
    negative = []
    for num in number:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)  
    return f"Positive: {positive} \n Negative: {negative}"

print(positive_or_negative(number_list))

# შეიძლება ასეც: print(positive_or_negative([1, 5, -34, -11, 92, -72, 84, 9, -46, -123, 3]))