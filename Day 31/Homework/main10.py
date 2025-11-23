# 10)ფუნქცია რომელიც იღებს რიცხვების სიას და ბეჭდავს მხოლოდ დადებითი რიცხვების ჯამს

def positive_numbers_summed(numbers):
    positive_nums = []
    for num in numbers:
        if num > 0:
            positive_nums.append(num)
    return sum(positive_nums)

print(positive_numbers_summed([1, 6, -2, -5, 7, 3, -10]))