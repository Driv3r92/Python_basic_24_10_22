# PEP8

"""
int - это целое число
float  - Это дробное число
str    - Это строка
bool - boolean всего 2 значения Истина = True Ложь= False
"""

catalog_id_1 = 14   # Это комментарий
catalog_id_2 = 15
my_float = 12.134
my_str1 = 'Это строка 1'
my_str2 = "Это тоже строка 2"
my_str3 = """"Это строка из множества строк"""

my_str4 = 'нужно выделить "ТЕРМИН"'
my_str5 = "нужно выделить \"ТЕРМИН\""\

# age = 18
# if age >= 18:
#     print('Доступ разрешен')
#     if age == 33:
#         print ('XXX')
# elif age >= 16:
#     print('Ограниченный доступ')
# else:
#     print('Доступ запрещен')
#
# while True:
#     age = input('Введите возраст\n')
#     if age.isdigit():
#         age = int(age)
#         break
#     print('Возраст должен быть числом')
#
# if age >= 18:
#     print('Доступ разрешен во все разделы включая ХХХ')
# elif age >= 16:
#     print('Доступ разрешен во все отделы')
# elif age >= 8:
#     print('Доступ разрешен в раздел мультиков')
# else:
#     print('Доступ запрещен')

# while True:
#     user = input()
#     if user == 'a':
#         continue
#     print (user)

name = 'USER'
surname = 'LAMER'
age = 16
'Пример User, тебе 16 лет твоя фамилия LAMER'

result = 'Пример {n:^20}, тебе {a} лет твоя фамилия {s}'.format(a=age, n=name, s=surname )
f_result = f'Пример {name:^20}, тебе {age} лет твоя фамилия {surname}, {2020 - age} года рождения'
print(f_result)