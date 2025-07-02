# პირველი დავალება 1) :



# Data coversation - არის მონაცემთა ტიპების შეცვლა.

# explicit - ეს ნიშნავს მონაცემის ტიპის შეცვლას ხილულად.. ეს ხდება ფუნქციების გამოყენებით  (  int()) , float() , str() , bool())    )
#           მაგალითად : 

age = "15"
height = "175.0"
weight = 53.4


print(int(age))
print(float(height))
print(str(weight))

# ეს არის explicit.

# //////////////////////////////////////////////////////////////////////////

# implicit - ეს ნიშნავს მონაცემების ტიპის შეცვლა ფარულად... როდესაც ჩვენ არ ვიყენებთ ფუნქციებს რომ შევცვალოთ.
#    მაგალითად :

x = 15 # integer

print("ეს არის Before implicit data conversation")

print(x)                # Before
print(type(x))
x = x/6 # გაყოფით გადაიქცა float - ად.


print("ეს არის After Implicit data conversation")

print(x)                # After
print(type(x))

#  გადაიქცა float - ად.


# დავალება 3) : Explicit Type Converation - ის ოთხი მაგალითი:

#  1)   int()
#  2)   bool()
#  3)   str()
#  4)   float()


#  Implicit Type Conversation - ის ხუთი მაგალითი:

# 1)    / - ზუსტი გაყოფა.
# 2)    // - გაყოფა , გამოიტანს წილად რიცხვს float - ს.
# 3)    % - გაყოფის დროს გვიბრუნებს ნაშთს.
# 4)    * - გამრავლება.
# 5)    ** - ხარისხი.

# ////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////

# რა არის Concatenation :

# კონკატენაცია არის ორი სტრინგის შეერთება:

# მაგალითად:
a = "star"
b = "wars"

print(a + b)

# შეერთდა სტრინგები - starwars


# ////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////

# 6) :

current_year = 2025
birth_year = int(input("Enter Your birth year :"))
age = current_year - birth_year

print(age)


name = "my name is luka"
surname = "my surname is misheladze , my age is"
age = "15"
a = "my height is"
height = "175.4"
b = "Im from"
address = "kazerti"

print(name + " " + surname + " " + age + " " + a + " " + height + " " + b + " " + address)

