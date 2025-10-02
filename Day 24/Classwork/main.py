programming_languages = ["pyhon" , "JavaScript" , "C++" , "HTML" , "CSS"]
print("Before: ")
print(programming_languages)

programming_languages.append("C#")
programming_languages.insert(2, "Ruby")
programming_languages.pop(3)
programming_languages.remove("CSS")

print("")
print("After:")
print(programming_languages)
print(len(programming_languages))