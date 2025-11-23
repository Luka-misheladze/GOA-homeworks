# 5)შექმენით ფუნქცია რომლსაც გადაეცემა რენდომ რიცხვების სია,
# ამ ფუნქციამ უნდა დააბრუნს სხვა სია სადაც ეს ელემენტები გაორმაგდებიან ([1, 4, 7] → შედეგი:[2, 8, 14])

numbers = [5, 12, 50, 22, 10, 15]

def double_nums(nums):
    double = []
    for num in nums:
        double.append(num * 2)
    return double

print(double_nums(numbers))