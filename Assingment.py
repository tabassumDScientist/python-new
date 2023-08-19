Python Programming Language Assignmnet # 3:
# 1.	Write a Python program to print the following string in a specific format (see the output). Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high \n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# 2.	Write a Python program to get the Python version you are using
#         import sys
# print("Python version")
# print (sys.version)
#      print("Version info.")
#       print (sys.version_info)
# 3.	Write a Python program to display the current date and time.
# import datetime

# x = datetime.datetime.now()
# print(x)
# 4.	Write a Python program which accepts the radius of a circle from the user and compute the area.
# r= float(input("Enter radius")) a=3.14*r*r 
# print("Area of the circle",a)
# 5.	Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
#  Fname= str(input("Enter your first name")) Lname= str(input("Enter yourLast name")) print("Hi"+Lname+Fname)
# 6.	Write a python program which takes two inputs from user and print them addition
# num1= int(input("Enter first number "))
#  num2= int(input("Enter 2nd number ")) 
# Add=num1+num2
#  print("sum two numbers :",Add) 
# 7.	Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ? 
# print(" Enter Mrks obtain in 5 sub") subj1=int(input()) subj2=int(input()) subj3=int(input()) subj4=int(input()) 
# subj5=int(input())
#  total=subj1+subj2+subj3+subj4+subj5
#  perc=(total/5)*300 perc =int(input())
#  if perc <=100 and perc >=80: 
# print("this is your grade :A+") 
# elif perc <=80 and perc >=70: 
# print("this is your grade :A") 
# elif perc <=70 and perc >=65: 
# print("this is your grade :B+")
#  elif perc <=64 and perc >=60: 
# print("this is your grade :B")
#  elif perc <=59 and perc >=50: 
# print("this is your grade :C+")
#  elif perc <=49 and perc >=40: 
# print("this is your grade :D+") 
# elif perc <=39 and perc >=30:
#  print("this is your grade :D") 
# elif perc <100 or perc<0:
#      print(“this is not valid”)
# else:
# print(“failed”)
# 8.	Write a program which take input from user and identify that the given number is even or odd?
# num=int(input("Enter any nmber to identify the number is odd or even"))
#  if(num%2)==0: 
# print("the number is even")
# else: print("the number is odd"

#  9. Write a program which print the length of the list?
# tab = ["apple", "banana", "cherry"]
# print(len(tab))
	
#  10.Write a Python program to sum all the numeric items in a list?
# a = [1, 2, 3, 4, 5]
# tab = sum(a)
# print(tab
#  11.Write a Python program to get the largest number from a numeric list. 
# #largest element in list

# #function
# def largest(list):
#     large= list[0]
#     for i in list:
#         if i>large:
#             large=i
#     return large

# #list
# list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
# print("largest in ",list,"is")
# print(largest(list))
# 12. Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] Write a program that prints out all the elements of the list that are less than 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# numbers = int(input("Pick a number: "))
# new_list = []
# for item in a:
#     if item < numbers:
#         new_list.append(item)
#     print(new_list)

# Assignment # 4 
# 1.	Make a calculator using Python with addition , subtraction , multiplication ,division and power.
# # This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(1/2/3/4): ")

#     # check if choice is one of the four options
#     if choice in ('1', '2', '3', '4'):
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")
# 2.	Write a program to check if there is any numeric value in list using for loop.

# tab =[1,2.5, False]
# for i in tab:
#     if type(i)in (int,float):
#         print("yes")
# else:
#     print("no")
# 3.	Write a Python script to add a key to a dictionary.
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# 4.	Write a Python program to sum all the numeric items in a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}
# print(sum(my_dict.values()))

# 5.	Write a program to identify duplicate values from list. 
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
# 6.	Write a Python script to check if a given key already exists in a dictionary.
#  Adict = {'Mon':3,'Tue':5,'Wed':6,'Thu':9}
#  print("The given dictionary : ",Adict) check_key = "Wed"
#  if check_key in Adict
#  keys(): print(check_key,"is Present.") 
# else: print(check_key, " is not Present.")
