# arguments.py

# --------------------------------
# 1. Parameter and Argument
# --------------------------------

# name হলো Parameter
def greet(name):
    print("Hello", name)


# "Udoy" হলো Argument
greet("Udoy")


# --------------------------------
# 2. Multiple Arguments
# --------------------------------

def add(a, b):
    print("Sum =", a + b)


add(10, 20)


# --------------------------------
# 3. Multiple Parameters
# --------------------------------

def student_info(name, age, department):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)


student_info("Udoy", 21, "CSE")


# --------------------------------
# 4. Default Argument
# --------------------------------

# যদি country না দেওয়া হয়,
# তাহলে Bangladesh automatically use হবে

def introduce(name, country="Bangladesh"):
    print("Name:", name)
    print("Country:", country)


introduce("Udoy")
introduce("Rahim", "India")


# --------------------------------
# 5. Keyword Argument
# --------------------------------

def person(name, age):
    print(name, "is", age, "years old")


# এখানে parameter-এর নাম বলে value দিচ্ছি
person(age=21, name="Udoy")


# --------------------------------
# 6. *args
# --------------------------------

# *args ব্যবহার করলে অনেকগুলো argument
# একসাথে নেওয়া যায়

def total(*numbers):

    sum = 0

    for number in numbers:
        sum += number

    print("Total =", sum)


total(10, 20)
total(10, 20, 30)
total(10, 20, 30, 40, 50)


# --------------------------------
# 7. **kwargs
# --------------------------------

# **kwargs অনেকগুলো keyword argument নেয়

def show_info(**info):

    for key, value in info.items():
        print(key, ":", value)


show_info(
    name="Udoy",
    age=21,
    department="CSE"
)