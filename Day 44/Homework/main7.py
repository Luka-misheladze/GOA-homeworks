# 10) დაწერეთ პროგრამა, რომელიც გამოთვლის კენტი რიცხვების ჯამს
# 1-დან 100-მდე და დაბეჭდავს შედეგს.

odd_count = 0
for i in range(1, 100, 2):
    odd_count = odd_count + i

print(odd_count)