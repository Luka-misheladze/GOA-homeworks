def biggest_number(num, num1, num2):
    if num2 > num1 and num2 > num:
        return(f"biggest number is: {num2}")
    elif num1 > num2 and num1 > num:
        return(f"biggest number is: {num1}")
    else:
        return(f"biggest number is: {num}")
    
print(biggest_number(715, 123, 871))

# შეგვიძლია ასეც მეორენაირად: 

def biggest_num(num, num1, num2):
    return max(num, num1, num2)

print(biggest_num(871, 719, 832))