# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        weight_score_dict = json.load(f)  # загнали все, что получилось в переменную
    sum = 0
    for elem in weight_score_dict:
        sum += elem['score'] * elem['weight']
    return round(sum, 3)


print(task())
