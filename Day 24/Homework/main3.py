# შექმენი სია სადაც შეინახავ ადამიანების სახელებს, რომლებიც გინდა, რომ დაპატიჟო წვეულებაზე,
# შენი მიზანია გაფილტრო ეს ადამიანები, ზოგი ამოშალო ზოგი დაამატო(append , pop , insert)
# ბოლოს უნდა დაბეჭდო ყველანაირი ინფორმაცია.

# 1)თავდფაპირველი სია
# 2)ამოკლებული ადამიანები
# 3)დამატებული ადამიანები
# 4)რამდენი ადამიანი დარჩა სულ
# 5)საბოლოო სია

birthday_list = ["luka" , "andria" , "nika" , "miriani" , "gio" , "lasha" , "mate"]

print("")
print("First birthday list:" , birthday_list)
print("")

removed_people = birthday_list.pop(3)
print("People i removed:" , removed_people)

added_person1 = "rezi"
added_person2 = "giga"
birthday_list.append(added_person1)
birthday_list.insert(5, added_person2)

print("People I added:" , added_person1 , added_person2 )

how_many_left = len(birthday_list)
print("how many people are left in the party list:" , how_many_left)

print("")
print("last list:" , birthday_list)
print("")