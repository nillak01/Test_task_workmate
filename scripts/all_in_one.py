import argparse
import csv
from collections import defaultdict
from statistics import median, mean, mode
from tabulate import tabulate


def get_pars():
    # Создаем парсер
    parser = argparse.ArgumentParser(
        description='Мой скрипт для обработки данных'
        )

    # Добавляем аргументы
    parser.add_argument('--files', nargs='+', help='Название файлов')
    parser.add_argument('--report', type=str, help='Название отчетов')
    parser.add_argument('--output', type=str,
                        help='Название файла для сохранения отчета')

    # Парсим аргументы
    return parser.parse_args()


def read_csv(files: list):

    students_dict = defaultdict(list)

    # Чтение с заголовками (как словарь)
    for path in files:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for index, row in enumerate(reader):
                    # Если значение не удается превести в int записываем 0
                    try:
                        students_dict[row['student']].append(
                            int(row['coffee_spent'].replace(' ', '0'))
                            )
                    except Exception as e:
                        print(e)
                        students_dict[row['student']].append(0)
        except Exception as e:
            print(e)

    return students_dict


def get_median_coffe_report(students_dict: dict):

    med_report = []
    for name in students_dict:
        med_report.append([name, median(students_dict[name])])

    return med_report


def get_mean_coffe_report(students_dict: dict):

    mean_report = []
    for name in students_dict:
        mean_report.append([name, mean(students_dict[name])])

    return mean_report


def get_mode_coffe_report(students_dict: dict):

    mode_report = []
    for name in students_dict:
        mode_report.append([name, mode(students_dict[name])])

    return mode_report


def show_table(data: list, headers: list):

    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)


def run():

    reposrts_dict = {
        'median-coffee': get_median_coffe_report,
        'mean-coffee': get_mean_coffe_report,
        'mode-coffee': get_mode_coffe_report,
    }

    args = get_pars()
    # Задаем название для отчета по умолчанию
    report_name = args.report if args.report else 'median-coffee'
    # Заголовки столбцов для вывода
    headers = ["student", args.report]
    students_dict = read_csv(args.files)
    data = reposrts_dict[report_name](students_dict)
    show_table(data, headers)
