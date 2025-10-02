# 4)სიიდან ამოარჩიეთ ლუწი რიცხვები და შემდეგ sum ცვლადში დააჯამეთ

list = [4 , 5 , 1 , 7 , 512 , 123 , 812 , 19 , 10]
sum = 0

for i in list:
    if i % 2 == 0:
        print(i)
        sum = sum + i

print("everything summed: " , sum)