users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
stat_of_visit = {"Общее количество": 0, "Уникальные посещения": 0}
stat_of_visit["Общее количество"] = len(users)
stat_of_visit["Уникальные посещения"] = len(set(users))
print(stat_of_visit)
