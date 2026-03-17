import argparse
import csv
import sys
from collections import defaultdict
from statistics import median, mean, mode
from tabulate import tabulate
from logger import logging


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


def process_cli_parser():

    args = get_pars()
    if not (args.files):
        logging.critical(
            """Критическая ошибка: не указан ни один файл.
                Отчет не может быть построен""")
        sys.exit(1)

    # Задаем название для отчета по умолчанию
    if args.report:
        report_name = args.report
    else:
        report_name = 'median-coffee'
        logging.warning(
            """Report не указан.
            Название устанавливается по умолчанию median-coffee""")
    output = args.output
    if (output is not None):
        output += output if output.find('.') != -1 else output + '.txt'

    return args.files, report_name, output


def show_table(data: list, headers: list, output: str | None = None):

    if data:
        table = tabulate(data, headers=headers, tablefmt="grid")
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(table)
        print(table)


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
                    except Exception:
                        logging.info(
                            f"""В файле {path} ошибочное значение
                             поля coffee_spent"""
                            )
                        students_dict[row['student']].append(0)
        except Exception:
            logging.warning(f"Предупреждение: файл {path} не найден")

    return students_dict


def get_median_coffe_report(students_dict: dict) -> list:

    med_report = []
    for name in students_dict:
        med_report.append([name, median(students_dict[name])])

    return med_report


def get_mean_coffe_report(students_dict: dict) -> list:

    mean_report = []
    for name in students_dict:
        mean_report.append([name, mean(students_dict[name])])

    return mean_report


def get_mode_coffe_report(students_dict: dict) -> list:

    mode_report = []
    for name in students_dict:
        mode_report.append([name, mode(students_dict[name])])

    return mode_report


def run():

    reports_dict = {
        'median-coffee': get_median_coffe_report,
        'mean-coffee': get_mean_coffe_report,
        'mode-coffee': get_mode_coffe_report,
        'another': get_median_coffe_report,
    }

    files, report_name, output = process_cli_parser()
    # Заголовки столбцов для вывода
    headers = ["student", report_name]
    students_dict = read_csv(files)
    try:
        reports_dict[report_name]
        data = reports_dict[report_name](students_dict)
    except Exception:
        data = reports_dict['another'](students_dict)
    show_table(data, headers, output)
