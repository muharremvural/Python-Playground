# INTERVIEW PRACTICE QUESTIONS #

# Tuple and List difference?
# Tuple can't be changed, we prefer tuple in situations where we don't want values to be changed.

# Celcius to Kelvin convertor function

def convertor(temp):
    return temp + 273


# Write a function with age argument,
# for age 18 or below output is "you cannot enter"
# for greater than 18 output is "welcome"

def age_check(age):
    if age <= 18:
        print("you cannot enter")
    elif age > 18:
        print("welcome")


# Checking whether the course is mathematics or not by using the following variables, and printing the statement "Math exam is announced" if it is mathematics,
# if the subject is mathematics, also checking whether the score is greater than 65 and
# If greater than 65, write the codes that output 'You Passed the Exam'.

def exam_check(subject, score):
    if subject.lower() == "mathematics":
        print("Math exam is announced")
        if score > 65:
            print("You passed the exam")
        elif score <= 65:
            print("You failed the exam")
    else:
        print("Exam has not been announced")


# Move the elements in list A given below to list B using the for loop.

A = [10, 11, 12, 13, 14, 15, 16]
B = []


def move(list_source, list_sink):
    list_sink = []
    for i in list_source:
        list_sink.append(i)
    return list_source, list_sink


list_source, list_sink = move(A, B)


# Seperate Numbers from 1 to 50 as even and odd

def sep_evenodd(tonumber):
    even_list = []
    odd_list = []
    for number in range(tonumber):
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return even_list, odd_list


even_list, odd_list = sep_evenodd(50)


# Write a function to take the power of two given numbers.

def square(a, b):
    return a ** b


# Write a function to sum every number in a given list.

def summer(list):
    list = []
    for num in list:
        sum += num
    return sum


list1 = [0, 2, 5, 6, 98, 4, 5]

# Write a function to display unique numbers in a given list.

non_unique = [1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8]


def find_uniques(listu):
    return list(set(listu))


# Write a function to calculate factorial of a given number with for loop.

def factorial(a: int):
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact


# Use args to summer function

def sumargs(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


# Return words from a list which are longer than 5 characters.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

[f for f in fruits if len(f) > 5]
