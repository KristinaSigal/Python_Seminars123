# 2. Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def CheckPredikat():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
                if not (not (x or y or z) == (not x and not y and not z)):
                    return 'Не для всех значений предикат утверждение истинно'
    return 'Для всех значений предикат утверждение истинно'
print(CheckPredikat())