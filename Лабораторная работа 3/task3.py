def count_letters(text: str):
    text = text.lower()
    dict_of_letters = {}
    for symbol in text:
        if symbol.isalpha():
            if symbol in dict_of_letters:
                dict_of_letters[symbol] += 1
            else:
                dict_of_letters[symbol] = 1
    return dict_of_letters


def calculate_frequency(dict_of_letters: dict):
    sum_letters = sum(dict_of_letters.values())
    for key in dict_of_letters:
        dict_of_letters[key] /= sum_letters
    return dict_of_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dict_of_letters = count_letters(main_str)
freq_dict = calculate_frequency(dict_of_letters)
for key in freq_dict:
    print(f'{key}: {round(freq_dict[key], 2):.2f}')
