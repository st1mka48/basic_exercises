from collections import Counter
#
# # Задание 1
# # Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# # Пример вывода:
# # Вася: 1
# # Маша: 2
# # Петя: 2
#
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

#

def count_name():
    dic = []
    for i in students:
        dic.append(i['first_name'])
    name = Counter(dic)
    for j in name:
        print(j,name[j])

# count_name()

# # Задание 2
# # Дан список учеников, нужно вывести самое часто повторящееся имя
# # Пример вывода:
# # Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
#
#
def repeat():
    my_list = []
    count = 0
    n = ''
    for i in students:
        my_list.append(i['first_name'])
    name = Counter(my_list)
    for j in name.most_common():
        if j[1] > count:
            count = j[1]
            n = j[0]
    print(f'Самое частое имя среди учеников: {n}')
repeat()
#
# # Задание 3
# # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# # Пример вывода:
# # Самое частое имя в классе 1: Вася
# # Самое частое имя в классе 2: Маша
#
# school_students = [
#     [  # это – первый класс
#         {'first_name': 'Вася'},
#         {'first_name': 'Вася'},
#     ],
#     [  # это – второй класс
#         {'first_name': 'Маша'},
#         {'first_name': 'Маша'},
#         {'first_name': 'Оля'},
#     ], [  # это – третий класс
#         {'first_name': 'Женя'},
#         {'first_name': 'Петя'},
#         {'first_name': 'Женя'},
#         {'first_name': 'Саша'},
#     ],
# ]
#
#
# def repeat_name():
#     for i, class_students in enumerate(school_students):
#         names = [student['first_name'] for student in class_students]
#         max_count = 0
#         max_name = ''
#         for name in names:
#             count = names.count(name)
#             if count > max_count:
#                 max_count = count
#                 max_name = name
#         print(f"Самое частое имя в классе {i + 1}: {max_name}")
#
#
# repeat_name()
#
# # Задание 4
# # Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# # Пример вывода:
# # Класс 2a: девочки 2, мальчики 0
# # Класс 2б: девочки 0, мальчики 2
#
# school = [
#     {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#     {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
#     {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
# ]
# is_male = {
#     'Олег': True,
#     'Маша': False,
#     'Оля': False,
#     'Миша': True,
#     'Даша': False,
# }
#
#
# def count_men_girl():
#     for all_class in school:
#         count_men = 0
#         count_girl = 0
#         for all_students in all_class['students']:
#             if is_male[all_students['first_name']]:
#                 count_men += 1
#             elif is_male[all_students['first_name']] == False:
#                 count_girl += 1
#         print(f"В классе {all_class['class']}: девочки {count_girl}, мальчики {count_men}")
#
#
# count_men_girl()
#
# # Задание 5
#
# # По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# # Пример вывода:
# # Больше всего мальчиков в классе 3c
# # Больше всего девочек в классе 2a
#
# school = [
#     {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
#     {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
# ]
# is_male = {
#     'Маша': False,
#     'Оля': False,
#     'Олег': True,
#     'Миша': True,
# }
#
#
# def all_man_girl():
#     man = 0
#     girl = 0
#     a_gilr = ''
#     a_man = ''
#     for all_class in school:
#         count_men = 0
#         count_girl = 0
#         for all_student in all_class['students']:
#             if is_male[all_student['first_name']] == True:
#                 count_men += 1
#             elif is_male[all_student['first_name']] == False:
#                 count_girl += 1
#         if count_girl > girl:
#             a_gilr = all_class['class']
#         elif count_men > man:
#             a_man = all_class['class']
#     print(f'Больше всего мальчиков в классе: {a_man}\n'
#           f'Больше всего девочек в классе: {a_gilr}')
#
#
# all_man_girl()
