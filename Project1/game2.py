"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def random_predict(number: int = 1) -> int:
    count = 0  #устанавливаем счетчик
    hi = 101   #определяем максимальную границу
    low = 1    #определяем минимальную границу
    predict = np.random.randint(low, hi) #генерируем отгадку
    
    while number != predict:
        count += 1
        if number > predict:
            low = predict    #сужаем нижнюю границу для генерации отгадки
            predict = np.random.randint(low, hi)
        elif number < predict:
            hi = predict     #сужаем верхнюю границу для генерации отгадки
            predict = np.random.randint(low, hi)
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []   # определяем пустой список для значений кол-ва отгадок
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:   #проходим по каждому значению из списка
        count_ls.append(random_predict(number))  #...и заносим ответ в наш список

    score = int(np.mean(count_ls))  # определяем среднее значение
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")

if __name__ == '__main__':
    score_game(random_predict)