print("---- Welcome to quiz master ----")
print("")
print("quick message - On each question choose it with A, B, C, or either with names.")
print("make sure to spell correctly otherwise system will take it as wrong answer!")
print("Which quiz do you want?")

print("")
print("1 easy quiz")
print("2 medium quiz")
print("3 hard quiz")
print("")

max_tries = 3
max_tries_medium = 4
max_tries_hard = 5

selection = input("Select Your quiz level: ")

if selection == "":
    print("Invalid Choice!")
elif selection == "1" or selection == "easy quiz" or selection == "easy".strip().lower():
    print("")
    print("Ur choice is easy quiz")
    print("U have 3 tries on the easy quiz.")
    print("But on each level tries will be more")
    print("")
    question_1 = input("Which one is programming language? HTML, CSS, Python: ").lower().strip()
    # Correct answer is python
    if question_1 == "python":
        print("ur correct!")
        print("")
    else:
        print("")
        print("Incorrect!")
        print(f"tries left = {max_tries - 1}")
        max_tries = max_tries - 1
        print("")

    question_2 = input("Which one of these is used for back-end: swift, css, ruby: ").lower().strip()
    # Correct answer is ruby
    if question_2 == "ruby":
        print("ur answer is correct!")
        print("")
    else:
        print("")
        print("incorrect!")
        print(f"tries left = {max_tries - 1}")
        print("")
        max_tries = max_tries - 1
        
    question_3 = input("Which one is used in front-end: c++, java, html: ").lower().strip()
    # correct answer is html
    if question_3 == "html":
        print("")
        print("correct! ➕")
        print("")
        print("----You've completed the easy quiz! congrats! 🎉 ----")
        print("----Now u can either choose another quiz or leave.----")
        print("")
    else:
        print("Incorrect!")
        print(f"tries left = {max_tries - 1}")
        max_tries = max_tries - 1
    if max_tries == 0:
        print("")
        print("quiz over ❌ start again!")
elif selection == "2" or selection == "medium quiz" or selection == "medium".strip().lower():
    print("")
    print("---- Ur choice is medium quiz, in medium quiz u have 4 tries ----")
    print("")
    question_4 = input("What is javascript used for?: backend, data analysis, api: ").strip().lower()
    # Correct answer is backend
    if question_4 == "backend":
        print("Ur correct!")
        print("")
    else:
        max_tries_medium = max_tries_medium - 1  
        print("ur wrong!")
        print(f"tries left: {max_tries_medium}")
        
    print("")
    question_5 = input("What does CSS stand for?: A) Cascading Style Sheets, B) Computer Styling System, C) Creative Sheet Setup: ").strip().lower()
    if question_5 == "a" or question_5 == "a) cascading style sheets" or question_5 == "cascading style sheets":
        print("Answer is correct!")
        print("")
    else:
        max_tries_medium = max_tries_medium - 1
        print("Incorrect!")
        print(f"Tries left: {max_tries_medium}")
        print("")

    question_6 = input("Which language is mainly used to build Android apps?: A) swift, B) Java, C) Ruby: ").strip().lower()
    if question_6 == "a" or question_6 == "a) swift" or question_6 == "swift":
        print("You are correct!!")
        print("")
    else:
        max_tries_medium = max_tries_medium - 1
        print("Incorrect!")
        print(f"Tries left: {max_tries_medium}")
        print("")

    question_7 = input("Which of these is a backend language?: A) php, B) html, C) kotlin: ").strip().lower()
    if question_7 == "a" or question_7 == "a) php" or question_7 == "php":
        print("Ur answer is Correct!!")
        print("")
    else:
        max_tries_medium = max_tries_medium - 1
        print("Incorrect!")
        print(f"Tries left: {max_tries_medium}")
        if max_tries_medium == 0:
            print("")
            print("---- quiz start over again or finish the quizes if u have any left! ----")
            exit()
    question_8 = input("What is the correct file extension for Python files?: A) .pt, B) .pyt, C) .py: ").strip().lower()
    if question_8 == "c" or question_8 == "c) .py" or question_8 == ".py" or question_8 == "py":
        print("U are correct!")
        print("")
        print("---- U successfully passed the medium quiz! Congrats 🎉 ----")
    else:
        max_tries_medium = max_tries_medium - 1
        print("Incorrect!")
        print(f"Tries left: {max_tries_medium}")
        if max_tries_medium == 0:
            print("")
            print("---- quiz failed ❌ start over again or finish the quizes if u have any left! ----")

elif selection == "3" or selection == "hard quiz" or selection == "hard":
    print("")
    print("---- This time you chose hard quiz ----")
    print("---- You have 5 tries on hard quiz now! ----")
    print("               Be Careful")
    print("")

    question_9 = input("What is the correct file extension for HTML?: .html, .htm, .ht: ").strip().lower()
    if question_9 == ".html":
        print("You are correct!")
    else:
        max_tries_hard = max_tries_hard - 1
        print("wrong answer!")
        print(f"Tries left: {max_tries_hard}")
    
    print("")
    question_10 = input("what does html mean A) High Transfer Markup Language B) Hyper Text Markup Language C) Hyper Trainer Markup Language: ").strip().lower()
    if question_10 == "b" or question_10 == "hyper text markup language":
        print("Your answer is correct good job!")
    else:
        max_tries_hard = max_tries_hard - 1
        print("Wrong answer!")
        print(f"Tries left: {max_tries_hard}")

    print("")
    question_11 = input("What does CSS control on a website?: A) The structure of the page, B) The styling and layout, C) The website’s data and logic: ").strip().lower()
    if question_11 == "b" or question_11 == "the styling and layout":
        print("you are correct, keep it up!")
    else:
        max_tries_hard = max_tries_hard - 1
        print("Wrong answer")
        print(f"Tries left: {max_tries_hard}")

    print("")
    question_12 = input("What does var do in JavaScript?: A) Declares a variable, B) Declares a function, C) Creates a loop: ").strip().lower()
    if question_12 == "a" or question_12 == "declares a variable":
        print("You are correct, ur so smart!")
    else:
        max_tries_hard = max_tries_hard - 1
        print("wrong answer!")
        print(f"Tries left: {max_tries_hard}")

    print("")
    question_13 = input("In Python, what does len() do?: A) Counts numbers, B) Returns the length of a list, string, or other iterable, C) Deletes a variable: ").strip().lower()
    if question_13 == "b" or question_13 == "returns the length of a list":
        print("You are correct, nice work!!")
    else:
        max_tries_hard = max_tries_hard - 1
        print("Incorrect!")
        print(f"Tries left: {max_tries_hard}")
        if max_tries_hard == 0:
            print("")
            print("---- Hard quiz failed! Try again ❌ ----")
            print("")
            exit()
        
    print("")   
    question_14 = input("What does z-index do in CSS?: A) Changes font size, B) Sets the stacking order of elements, C) Aligns text vertically: ").strip().lower()
    if question_14 == "b" or question_14 == "sets the stacking order of elements":
        print("Answer is correct! good joob!!")
        print("")
        print("---- Good job! You successfully passed the hard quiz ✅ ----")
        print("          ---- You are a true Developer 😁 ---- ")
        print("")
    else:
        max_tries_hard = max_tries_hard - 1
        print("Incorrect answer!")
        print(f"Tries left: {max_tries_hard}")
        if max_tries_hard == 0:
            print("U failed the Hard quiz, u can leave or choose any quiz that u have left.")