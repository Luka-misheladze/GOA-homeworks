list = [1 , 5 , 2 , 7 , 3 , 4 , 91 , 67 , 10 , 34]

sum = 0

for i in list:
    if i % 2 != 0:
        print(i)
        sum = sum + i

print("Everything summed:" , sum)