def find_common_participants(str1, str2, sep=","):
    participants_group1 = str1.split(sep)
    participants_group2 = str2.split(sep)

    common_participants = list(set(participants_group1).intersection(participants_group2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
paricipants = find_common_participants(participants_first_group, participants_second_group, "|")
print(paricipants)