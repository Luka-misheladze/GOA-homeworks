# 3) დაწერე ფუნქცია რომელიც პარამეტრად მიიღებს მომხმარებლის დაბადების წელს და გამოთვლის რამდენი წლისაა ის დღეს
def howold(birth_year):
    current_year = 2026
    age = current_year - birth_year
    return age

print(howold(2010))