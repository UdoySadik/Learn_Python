# functions.py


# --------------------------------
# 1. Simple Function
# --------------------------------

def hello():
    print("Hello Python!")


# Function call
hello()


# --------------------------------
# 2. Function with Parameter
# --------------------------------

def greet(name):
    print("Hello", name)


greet("Udoy")
greet("Rahim")


# --------------------------------
# 3. Function with Return
# --------------------------------

def add(a, b):

    result = a + b

    return result


answer = add(10, 20)

print("Answer =", answer)


# --------------------------------
# 4. Return vs Print
# --------------------------------

def square(number):

    return number * number


result = square(5)

print("Square =", result)


# --------------------------------
# 5. Function can be used
# inside another function
# --------------------------------

def double(number):
    return number * 2


def calculate(number):

    result = double(number)

    return result + 10


print(calculate(5))


# --------------------------------
# 6. Function with condition
# --------------------------------

def check_even(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even(10))
print(check_even(7))


# --------------------------------
# 7. Function with loop
# --------------------------------

def print_numbers(n):

    for i in range(1, n + 1):
        print(i)


print_numbers(5)