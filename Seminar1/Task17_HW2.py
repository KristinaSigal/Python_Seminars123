'''4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.'''

N = int(input('Введите число N: '))

def addLst(N):
    rng = range(-N, N)
    result = 1
    file = open('file.txt', 'r')
    for line in file:
        result *= rng[int(line)]
        print(f"{int(line)} -> {rng[int(line)]}")
    print(result)
    file.close()
    
addLst(N)