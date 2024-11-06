# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
    return letters_count

def calculate_frequency(letters_dict):
    data_freq = {}
    letters_in_text = 0
    for letter in main_str:
        if letter.isalpha():
            letters_in_text += 1
    for item in letters_dict:
        data_freq[item] = f"{round(letters_dict[item] / letters_in_text, 2):.2f}"
    return data_freq




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

# TODO Распечатайте в столбик букву и её частоту в тексте
count_ = count_letters(main_str)
frequency_ = calculate_frequency(count_)

for letter, frequancy in frequency_.items():
    print(letter + ": " + str(frequancy))