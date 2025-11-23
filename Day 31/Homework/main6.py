# 6)შექმენით ფუნქცია რომელსაც გადაეცემა რენდომ სია,
# ამ ფუნქციამ უნდა დააბრუნოს თავდაპირველი სია ოღონდ რევერსულად(შებრუნებული)
# ([1,4,7] → [7,4,1]

numbers = [10, 50, 24, 8, 6, 100]

def reversed_nums(nums):
    halved_nums = []
    for num in nums:
        halved_nums.append(num / 2)
    return halved_nums

print(reversed_nums(numbers))