#Задание 1

#  employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Malifisenta", "Juilet", "Moana"]

# print(employee_list[1] + ", " + employee_list[-2])

# DOMASHKA
# lst = [ '🍇', '🍑', '🍐', '🍊', '🍌', '🍎']

# print(lst[1])
# print(lst[-1])

#Задание 2

#  def dev_by_three(x):
#     return "Да" if x % 3 == 0 else "Нет"

# num = int(input("Введите число: "))
# result = dev_by_three(num)
# print(f"Делиться ли на три {num}? - {result}")

# DOMASHKA
# def is_year_leap(x):
#     return "True" if x % 4 == 0 else "False"

# num = int(input("Введите год: "))
# result = is_year_leap(num)
# print(f"Год {num} : {result}")


#Задание 3

# import math


# def min_boxes(thing):
#    return math.ceil(thing / 5)

# num_things = int(input("Введите количество предметов: "))
# print(f"Минимальное количество коробок: {min_boxes(num_things)}")

# DOMASHKA
# import math


# def square(side):
#    return math.ceil(side * side)

# num_side = float(input("Введите сторону квадрата: "))
# print(f"Площадь квадрата равна: {square(num_side)}")

#Задание 4


# n = int(input("Введите число:"))


# def check_divisibility(n):
#     for i in range(1, n + 1):
#         if i % 4 == 0:
#             print(f"{i} - Делится и на 2, и на 4")
#         elif i % 2 == 0:
#             print(f"{i} - Делится на 2, но не на 4")
#         else:
#             print(i)


# check_divisibility(n)

# DOMASHKA
# n = int(input("Введите число:"))

# def fizz_buzz(n):
#     for n in range(1, n + 1):
#         if n % 5 == 0 and n % 3 == 0:
#             print("FizzBuzz")
#         elif n % 3 == 0:
#             print("Fizz")
#         elif n % 5 == 0:
#             print("Buzz")      
        

#         else:
#             print(n)     
        
# fizz_buzz(n)

#Задание 5

# def quarter_of_year(n):
    
#     if 1 <= n <= 3:
#        return "I квартал"
#     elif 4 <= n <= 6:
#        return "II квартал"
#     elif 7 <= n <= 9:
#        return "III квартал"
#     elif 10 <= n <= 12:
#        return "IV квартал"
#     else:
#        return "Неверный номер месяца"
    
# try:
#    n = int(input("Введите номер месяца (1-12):"))
#    print(quarter_of_year(n)) 
# except ValueError:
#     print("Пожалуйста, введите целое число от 1 до 12.")

# DOMASHKA
# def monthon_to_season(n):
    
#     if 1 <= n <= 2:
#        return "Зима"
#     elif 3 <= n <= 5:
#        return "Весна"
#     elif 6 <= n <= 8:
#        return "Лето"
#     elif 9 <= n <= 11:
#        return "Осень"
#     elif n == 12:
#        return "Зима"
#     else:
#        return "Неверный номер месяца"
    
# try:
#    n = int(input("Введите номер месяца (1-12):"))
#    print(monthon_to_season(n)) 
# except ValueError:
#     print("Пожалуйста, введите целое число от 1 до 12.")
        


# Задание  6

# lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

# for n in lst:
# 	if (n % 3 == 0) and (n > 15):
# 		print(n)
		
# DOMASHKA

# lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

# for n in lst:
# 	if (n % 3 == 0) and (n < 30):
# 		print(n)


# Задание 7


# list = list(range(25, 0, -5))
# print(list)

# DOMASHKA

list = list(range(18, 0, -4))
print(list)

# Задание 8

# var_1 = 50
# var_2 = 5

# var_1, var_2 = var_2, var_1

# print(f"var_1= {var_1}, var_2= {var_2}")
 



