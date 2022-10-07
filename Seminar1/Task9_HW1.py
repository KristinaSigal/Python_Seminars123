# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarterNum = 0
while quarterNum < 1 or quarterNum > 4:
    quarterNum = int(input('Введите номер четверти от 1 до 4 для определения диапазона значений: '))

def GetRange(quarterNum):
    if quarterNum == 1:
        return 'Диапазон возможных координат точек: x > 0, y > 0'
    elif quarterNum == 2:
        return 'Диапазон возможных координат точек: x < 0, y > 0'
    elif quarterNum == 3:
        return 'Диапазон возможных координат точек: x < 0, y < 0'
    elif quarterNum == 4:
        return 'Диапазон возможных координат точек: x > 0, y < 0'

print(GetRange(quarterNum))