'''1. Напишите программу, которая 
* принимает на вход вещественное число и 
* показывает сумму его цифр.    
    Пример:    
    - 6782 -> 23
    - 0,56 -> 11'''

number = (input('Введите вещественное число '))

def sumDigit(number):
    sum = 0
    for i in number:
        if i != '.' and i != ',':
            sum = sum + int(i)
    return sum
print(f"Сумма цифр в числе {number} равна {sumDigit(number)}")