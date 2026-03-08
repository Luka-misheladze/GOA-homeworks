# 8) გამოიყენეთ for loop 4-ის გამრავლების ცხრილის დასაბეჭდად
# (4 × 1-დან 4 × 10-მდე).

def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
table(4)