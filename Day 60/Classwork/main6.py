
def even_odd(numbers):
    numbers.append(120)
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum = even_sum + num
    return even_sum

numbers = [10, 20 ,25, 29, 30, 48, 50]
result = even_odd(numbers)
print("ლუწების ჯამია:", result)