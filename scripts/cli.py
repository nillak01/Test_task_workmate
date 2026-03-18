import argparse
import sys
from tabulate import tabulate
from scripts.logger import logging


def get_pars(args=None):
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
    return parser.parse_args(args)


def process_cli_parser(args_base=None):

    args = get_pars(args_base)
    if not (args.files):
        logging.critical(
            """Критическая ошибка: не указан ни один файл. Отчет не может быть построен""")
        sys.exit(1)

    # Задаем название для отчета по умолчанию
    if args.report:
        report_name = args.report
    else:
        report_name = 'median-coffee'
        logging.warning(
            """Report не указан. Название устанавливается по умолчанию median-coffee""")
    output = args.output
    if (output is not None):
        output = output if output.find('.') != -1 else output + '.txt'

    return args.files, report_name, output


def show_table(data: list, headers: list, output: str | None = None):

    if data:
        table = tabulate(data, headers=headers, tablefmt="grid")
        if output:
            try:
                with open(output, "w", encoding="utf-8") as f:
                    f.write(table)
            except Exception:
                logging.error("""Упс.. Сохранение файла пошло не по плану""")
        print(table)
