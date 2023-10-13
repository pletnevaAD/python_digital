from collections import Counter


def find_common_participants(participants_first_group, participants_second_group, separator=','):
    first_group = participants_first_group.split(sep=separator)
    second_group = participants_second_group.split(sep=separator)
    counter = Counter(first_group + second_group)
    repeated_elements = sorted([item for item, count in counter.items() if count > 1])
    return repeated_elements



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
