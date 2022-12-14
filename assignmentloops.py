# 1. if -3 will evaluate to True
#  True
#  False
Answer = True


# 2. Given the nested if-else below, what will be the value x when the code executed successfully
# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)


#  0
#  4
#  2
#  3
 
Answer = 3


# 3. What is the output of the following nested loop?
# for num in range(10, 14):
#    for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break
#  Option 1: 10
#       11
#       12
#       13
# Option 2 :11
#     13

Answer = 10
         11
         12
         13

# 4. What is the output of the following loop
# for l in 'Jhon':
#    if l == 'o':
#       pass
#    print(l, end=", ")

#  J, h, n,
#  J, h, o, n,

Answer = J, h, o, n
 
 
 
# 5. What is the value of x after the following nested for loop completes its execution
# x = 0
# for i in range(10):
#   for j in range(-1, -10, -1):
#     x += 1
#     print(x)

#  99
#  90
#  100

Answer = 90



# 6. Select which is true for for loop
#  Python’s for loop used to iterates over the items of list, tuple, dictionary, set, or string
#  else clause of for loop is executed when the loop terminates naturally
#  else clause of for loop is executed when the loop terminates abruptly
#  We use for loop when we want to perform a task indefinitely until a particular condition is met

Answer = Python’s for loop used to iterates over the items of list, tuple, dictionary, set, or string
        else clause of for loop is executed when the loop terminates naturally

# 7. What is the output of the following if statement
# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#   print('False')

#  False
#  True

Answer = True



# 8. Given the nested if-else structure below, what will be the value of x after code execution completes
# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

#  2
#  0
#  3
#  4

Answer = 2

# 9. What is the output of the following for loop and  range() function
# for num in range(-2,-5,-1):
#     print(num, end=", ")

#  -2, -1, -3, -4
#  -2, -1, 0, 1, 2, 3,
#  -2, -1, 0
#  -2, -3, -4,

Answer = 2,1,0,-1,-2,-3,-4


# 10. What is the value of the var after the for loop completes its execution
# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)

#  20
#  21
#  10
#  30
 
Answer = 21
 
 
 
 
 
 
 
 
# 11. What is the output of the following nested loop
# numbers = [10, 20]
# items = ["Chair", "Table"]

# for x in numbers:
#   for y in items:
#     print(x, y)
# Option 1: 10 Chair
# 10 Table
# 20 Chair
# 20 Table
# Option 2 10 Chair
#     10 Table
# 12. What is the output of the following range() function
# for num in range(2,-5,-1):
#     print(num, end=", ")
#  2, 1, 0
#  2, 1, 0, -1, -2, -3, -4, -5
#  2, 1, 0, -1, -2, -3, -4 

answer=
 
 
 
 
 
 
# 13. What is the value of x
# x = 0
# while (x < 100):
#   x+=2
# print(x)
#  101
#  99
#  None of the above, this is an infinite loop
#  100

answer= 100




























# FUNCTIONS MCQ

# The quiz contains 13 Questions. Solve 8 correct to pass the test.
# You will have to read all the given answers and click over the correct answer.
 
# 1. What is the output of the following function call
# def fun1(name, age=20):
#     print(name, age)

# fun1('Emma', 25)
#  Emma 25
#  Emma 20
# 2. What is the output of the following display() function call
# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# display(emp="Kelly", salary=9000)
# option1. TypeError
# option2.  Kelly
#      	      9000
 
# option3. (’emp’, ‘Kelly’)
#     	    (‘salary’, 9000)
# option4. emp
#    	   salary
# 3. Select which is true for Python function
#  A Python function can return only a single value
#  A function can take an unlimited number of arguments.
#  A Python function can return multiple values
#  Python function doesn’t return anything unless and until you add a return statement
# 4. What is the output of the following code?
# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d
#     return inner_fun(a, b)

# res = outer_fun(5, 10)
# print(res)
#  15
#  Syntax Error
#  (5, 10)
# 5. What is the output of the add() function call
# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)
#  15
#  8
#  (8, 7)
#  Syntax Error
# 6. What is the output of the following function call
# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d

#     return inner_fun(a, b)
#     return a

# result = outer_fun(5, 10)
# print(result)
#  5
#  15
#  (15, 5)
#  Syntax Error
# 7. What is the output of the following display_person() function call
# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(name="Emma", age="25")
 
# Option 1 TypeError
# Option 2 Emma
#       25
# Option 3 name
#                age
# 8. Choose the correct function declaration of  fun1() so that we can execute the following function call successfully
# fun1(25, 75, 55)
# fun1(10, 20)
#  def fun1(**kwargs)
#  No, it is not possible in Python
#  def fun1(args*)
#  def fun1(*data)
# 9. Python function always returns a value
#  False
#  True
# 10. Given the following function fun1() Please select all the correct function calls
# def fun1(name, age):
#     print(name, age)
 
# 1.fun1("Emma", age=23)
#   2. fun1(age =23, name="Emma")
#  fun1(name="Emma", 23)
#  fun1(age =23, "Emma")
# 11. What is the output of the following function call
# def fun1(num):
#     return num + 25

# fun1(5)
# print(num)
#  25
#  5
#  NameError


# 12. Select which true for Python function
#  A function is a code block that only executes when called and always returns a value.
#  A function only executes when it is called and we can reuse it in a program
#  Python doesn’t support nested function
