# 5. Реализуйте алгоритм перемешивания списка.

from random import randint


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mix(lst):
    result = []
    while len(lst) > 0:
        index = randint(0, len(lst) - 1)
        result.append(lst[index])
        lst.remove(lst[index])
    print(result)
mix(list)