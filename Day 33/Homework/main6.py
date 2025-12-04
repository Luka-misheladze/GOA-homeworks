# 6) შექმენით ფუნქცია, რომელიც დააბრუნებს მასივში არსებული რიცხვების საშუალო არითმეტიკულს.


def arithmetic_average(num):
    return sum(num) / len(num)

print(arithmetic_average([12, 52, 122, 62, 72, 65, 5, 2, 7, 10]))