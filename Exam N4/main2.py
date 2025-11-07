def elections(age):
    if age >= 18:
        return("You can choose, ur and adult")
    else:
        return("ur not adult u cant choose")
    
print(elections(age=int(input("How old are you? : "))))