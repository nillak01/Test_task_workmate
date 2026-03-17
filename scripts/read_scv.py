import argparse
import csv
from collections import defaultdict
from statistics import median
from tabulate import tabulate



def get_pars():
    # Создаем парсер
    parser = argparse.ArgumentParser(description='Мой скрипт для обработки данных')

    # Добавляем аргументы
    parser.add_argument('--files', nargs='+', help='Название файлов')
    parser.add_argument('--report', type=str, help='Название отчетов')

    # Парсим аргументы
    return parser.parse_args()


def read_csv(files: list):

    students_dict = defaultdict(list)

    # Чтение с заголовками (как словарь)
    for path in files:
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader):
                students_dict[row['student']].append(
                    int(row['coffee_spent'].replace(' ', '0'))
                    )

    return students_dict


def get_median_coffe_report(students_dict: dict):
    
    med_report = []
    for name in students_dict:
        med_report.append([name, median(students_dict[name])])

    return med_report


def show_table(data: list, headers: list):

    table = tabulate(data, headers=headers, tablefmt="pipe")
    print(table)


def main():

    args = get_pars()

    # Заголовки столбцов для вывода
    headers = ["student", args.report]
    students_dict = read_csv(args.files)
    data = get_median_coffe_report(students_dict)
    show_table(data, headers)

    print(f"Обрабатываемые файлы: {args.files}")
    print(f"Результат сохраняем в: {args.report}")