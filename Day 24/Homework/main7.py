# 7)შექმენით სია სადაც იქნება ხილის ასორტი შენახული, ბევრნაირი ხილი მინიმუმ 10 სახეობა,
# თქვენი მიზანია სიის ფუქნციების მეშვეოით (append , insert , pop) გაფილტროთ ეს სია
# და დატოვოთ თქვენთვის Top 5 ხილი
# პრიორიტეტულად დალაგებული(1-5 ყველაზე => კარგი-ყველაზე ცუდი)

fruits = ["apple" , "banana" , "strawberry" , "orange" , "peach" , "Pineapple" , "watermelon" , "grape"]

print("")
print("before:" , fruits)

removed_fruits = fruits.pop(4)
removed_fruits_2 = fruits.pop(3)
added_fruit = "mango"
added_fruit_2 = "kiwi"
fruits.append(added_fruit_2)
fruits.insert(3, added_fruit)

print("")
print("after:" , fruits)
print("")