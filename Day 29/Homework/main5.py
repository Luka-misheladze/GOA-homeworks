# 5) დაწერეთ ფუნქცია arithmetic_average, და არგუმენტად გადაეცით რიცხვების სია.
# ფუნქციამ პასუხად უნდა დააბრუნოს რიცხვების საშუალო არითმეტიკული.

def arithmetic_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

nums = [5, 15, 50, 20, 10]
print(arithmetic_average(nums))