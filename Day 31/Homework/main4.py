# 4)შექმენით ფუნქცია რომელსაც გადაეცემა რენდომ სახელების სია,
# შემდეგ ამ ფუნქციამ უნდა დააბრუნოს მხოლოდ ის სახელები რომლებიც შეიცავენ 5 ან მეტ ასობგერას:

names = ["lika", "mari", "gabrieli", "dato", "demetre", "giorgi", "elene", "shio"]

for name in names:
    if len(name) >= 5:
        print(name)