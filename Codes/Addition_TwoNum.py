#1st method
# In this method Input are already declared with its variable 
# and a third variable namely sum which will add that two value stored in variable num1 and num2.
# here we can print the output by two ways as shown in following code.
# Both methods are commonly used, but the str.format() method offers more flexibility and readability,
# especially when dealing with multiple variables or more complex formatting.
num1 = 13
num2 = 34

sum = num1+num2
print("the sum of two numbers is",sum)
print("sum of {0} and {1} is {2}".format(num1,num2,sum))


#2nd method#taking input
# in this method the input is taken by the user.
# here we are taking input as a floating point for ensuring numeric addition, handling decimal number and avoiding type errors.
num1=input("\nenter first number = ")
num2=input("enter second number =")

sum=float(num1)+float(num2)

print("the sum of two numbers is=",sum)
print("the sum of {0} and {1} is {2}".format(num1,num2,sum))


#3rd method #using function
# in this method, we are using Function Definition, variable assignments, function call 
# and storing result and finally print the result.
def add(a,b):
    return a+b
num1 = 13
num2 = 34

sum_of_two_numbers = add(num1,num2)
print("\nsum of {0} and {1} is {2}".format(num1,num2,sum_of_two_numbers))


#4th methods
# in this code we have imported 'operator module' for addition purpose.
# in operator module we have used add function.
# operator.add(num1, num2) call the add function from module with num1 and num2 as arguments.
# then result is assigned to variable 'sum'
num1 = 32
num2 = 21

import operator
sum = operator.add(num1,num2)
print("the sum of",num1,"and",num2,"is",sum)


#5th method
# A lambda function is defined to add two numbers and is assigned to the variable 'add_numbers'.
# Two variables num1 and num2 are assigned the values 12 and 23, respectively.
# The lambda function 'add_numbers' is called with num1 and num2 as arguments, and the result is stored in the variable result.
# The result is printed to the console, showing the values of num1, num2, and their sum.
add_numbers = lambda x,y: x+y
num1 = 12
num2 = 23

result = add_numbers(num1,num2)
print("the sum of",num1,"and",num2,"is",result)


#6th method
# The function add_numbers_recusrisve is defined to add two numbers using recursion.
# The base case checks if y is zero; if it is, the function returns x.
# The recursive case increments x by 1 and decrements y by 1, calling the function recursively until y becomes zero.
# Variables num1 and num2 are assigned the values 34 and 21, respectively.
# The recursive function is called with num1 and num2, and the result is stored in the variable result.
# The result is printed, showing the values of num1, num2, and their sum.
def add_numbers_recusrisve(x,y):
    if y == 0:
        return x
    else:
        return add_numbers_recusrisve(x+1,y-1)

num1 = 34
num2 = 21

result = add_numbers_recusrisve(num1,num2)
print("the sum of",num1,"and",num2,"is",result)