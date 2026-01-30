#сгенерить 3д матрицу
#Создать алгоритм по поиску цифр
#посчитать время выполнения работы и оперативную память

import numpy as np
import time

matrix_3d = np.random.randint(0, 10, size=(3, 3, 3))
print(matrix_3d)

target = int(input('Выберите число которое хотите найти: '))
found = False

start_time = time.time()
for i in range(len(matrix_3d)):
    for j in range(len(matrix_3d[i])):
        for z in range(len(matrix_3d[i][j])):
            if matrix_3d[i][j][z] == target:
                print(f"Найдено: слой {i}, строка {j}, столбец {z}")
                found = True
if not found:
    print("Функция не справилась :( Число не найдено")
end_time = time.time()
duration = end_time - start_time

print(f"Функция справилась!!! Затрачено времени: {duration:.8f} сек.")
