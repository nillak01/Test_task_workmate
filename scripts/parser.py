import argparse


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
