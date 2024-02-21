# 1.
# P = float(input("Enter a Price : "))
# R = float(input("Enter a Rate : "))
# N = float(input("Enter a Time in month : "))
# simple_interest = P*R*(N/12)/100
# print("simple interest : ",simple_interest)
# print("All Amount with simple interest is : ",simple_interest+P)
# ==================================================================

# 2.
# first = float(input("Enter first Number : "))
# Second = float(input("Enter Second Number : "))
# print("Addition of Two number : ",first+Second)
# print("Subtraction of Two number : ",first-Second)
# print("Multiplication of Two number : ",first*Second)
# print("Division of Two number : ",first/Second)
# ==================================================================

# 3.
# sub1= float(input("Enter subject 1 Mark :"))
# sub2= float(input("Enter subject 2 Mark :"))
# sub3= float(input("Enter subject 3 Mark :"))
# sub4= float(input("Enter subject 4 Mark :"))
# total = sub1+ sub2 + sub3 + sub4
# percentage = total/4
# grade = 0 
# print("Total : " , total)
# print("Percentage : " ,percentage)
# if sub1< 39 and sub2< 39  and sub3< 39 and sub4< 39 :
#     if percentage >= 90 and percentage <= 100:
#         print("Grade A+")
#     elif percentage >= 80 and percentage <= 90:
#         print("Grade A")
#     elif(percentage >= 70 and percentage <= 80):
#         print("Grade B")
#     elif(percentage >= 60 and percentage <= 70 ):
#         print("Grade C")
#     elif(percentage >= 50 and percentage <= 60 ):
#         print("Grade D")
#     elif(percentage >= 40 and percentage <= 50 ):
#         print("Grade E")
# else:
#         print("FAIL")
# ==================================================================

# 4.
# def chk_armstrong(num):
#     sum = 0
#     for i in num:
#         sum += int(i) ** len(num)
#     return sum == 5
# arr = [input(f"ENTER NUMBER {i+1} : ") for i in range(10)]
# print(arr)
# for i in arr:
#     if chk_armstrong(i):
#         print("NUMBER IS ARMSTRONG", i)
#     else:
#         print("NUMBER NOT ARMSTRONG", i)
# ==================================================================

# 5.
# lst=[1,2,3,4,5,6,7,8,9,10] 
# num= 0
# for i in range(10):
#     lst.insert(i,int(input("ENTER NUMBER : ")))
# for i in lst:
#     if(i%2!=0):#odd
#         if(num<i):#max
#             num=i
# print(num)
# ==================================================================

# 6.
# arr = [4,9,7]
# for i in arr:
#     print("*"*i)
# ==================================================================

# 7.
# size = int(input("ENTER SIZE OF LIST : "))
# list1 = []
# for i in range(size):
#     list1.append(input(f"ENTER NUMBER {i+1} : "))
# print(list1)
# #create switch case for list operation
# print("1. APPEND")
# print("2. INSERT")
# print("3. REMOVE")
# print("4. POP")
# print("5. COUNT")
# print("6. EXTEND")
# print("7. INDEX")
# print("8. REVERSE")
# print("9. SORT")
# print("10. LEN")
# print("11. MAX")
# print("12. MIN")
# print("13. SUM")
# print("14. DEL")
# print("15. COPY")
# print("16. CLEAR")
# print("17. EXIT")

# while True:
#     choice = int(input("ENTER CHOICE : "))
#     if choice == 1:
#         value = input("ENTER NUMBER : ")
#         list1.append(value)
#         print(list1)
#     elif choice == 2:
#         position = int(input("ENTER POSITION : "))
#         value = input("ENTER VALUE : ")
#         list1.insert(position,value)
#         print(list1)
#     elif choice == 3:
#         value = input("ENTER VALUE : ")
#         list1.remove(value)
#         print(list1)
#     elif choice == 4:
#         list1.pop()
#         print(list1)
#     elif choice == 5:
#         value = input("ENTER VALUE : ")
#         print(list1.count(value))
#     elif choice == 6:
#         list2 = []
#         for i in range(3):
#             list2.append(input(f"ENTER NUMBER {i+1} : "))
#         list1.extend(list2)
#         print(list1)
#     elif choice == 7:
#         value = input("ENTER VALUE : ")
#         print(list1.index(value))
#     elif choice == 8:
#         list1.reverse()
#         print(list1)
#     elif choice == 9:
#         list1.sort()
#         print(list1)
#     elif choice == 10:
#         print(len(list1))
#     elif choice == 11:
#         print(max(list1))
#     elif choice == 12:
#         print(min(list1))
#     elif choice == 13:
#         for i in range(len(list1)):
#             list1[i] = int(list1[i])
#         print(sum(list1))
#     elif choice == 14:
#         position = int(input("ENTER POSITION : "))
#         del list1[position]
#         print(list1)
#     elif choice == 15:
#         list2 = list1.copy()
#         print(list2)
#     elif choice == 16:
#         list1.clear()
#         print(list1)
#     elif choice == 17:
#         break
#     else:
#         print("INVALID CHOICE")
# ==================================================================

# 8.
# str1 = input("ENTER STRING :- ")
# LENGTH = 0
# count=0
# for i in str1:
#     LENGTH += 1
#     if(i in 'aeiou'):
#         count += 1

# print("COUNT OF VOWEL ",count)
# print("LENGTH OF STRING : ",LENGTH)  
# # revers string
# reversedstr = str1[::-1]
# print("REVERSED STRING : ",reversedstr)
# # find and repace
# print(str1.replace('a','*'))
# # palindrom of not
# if(str1==reversedstr):
#     print("PALINDROM")
# else:
#     print("NOT PALINDROM")
# ==================================================================

# 9.
# write a program to create a function which accepts 2 numbers and one arithmatic operator. return the answer accordingly.
def arithmatic(num1,num2,operator):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    else:
        return "INVALID OPERATOR"
num1 = float(input("ENTER NUMBER 1 : "))
num2 = float(input("ENTER NUMBER 2 : "))
operator = input("ENTER OPERATOR : ")
print(arithmatic(num1,num2,operator))
# ==================================================================

# 10.




# ==================================================================

# 11.
# def total(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(total(1,2,3,4,5,6,7,8,9,10))
# ==================================================================

# 12.
# x = 10
# def outer():
#     x = 20
#     def inner():
#         nonlocal x
#         x = 30
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()
# print("global:", x)
# ==================================================================

# 13.
# write a program to make use of map(), filter() and reduce() functions with context to lamda function.
