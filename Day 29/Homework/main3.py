# 3) შექმენით ფუნქცია user_info, რომელსაც გადაეცემა სამი არგუმენტი: name, surname, address.
# return-ს გამოყენებით დააბრუნეთ მომხმარებლის ინფორმაცია შემდეგ ფორმატში:

# მომხმარებლის სახელი: <name>
# მომხმარებლის გვარი: <surname>
# მომხმარებლის მისამართი: <address>

def user_info(name, surname, address):
    return f"მომხმარებლის სახელი: {name} მომხმარებლის გვარი: {surname} მომხმარებლის მისამართი: {address}"

print(user_info("Luka" , "Misheladze" , "Georgia, Kazreti"))