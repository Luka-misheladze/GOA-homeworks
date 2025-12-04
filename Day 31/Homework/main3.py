# 3)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია , ამ ფუნქციამ უნდა დააბრუნოს ამ რიცხვების ჯამი:

numbers_list = [213, 51, 81, 45, 2, 7, 12]
def summed_numbers(final_number):
    number_sum = 0
    for num in final_number:
        number_sum += num
    return number_sum

print(summed_numbers(numbers_list))