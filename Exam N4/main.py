def odd_even(num):
    if num % 2 == 0:
        return("even")
    else:
        return("odd")
    
print(odd_even(num=int(input("choose a number: "))))