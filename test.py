import argparse
import csv

# Создаем парсер
parser = argparse.ArgumentParser(description='Мой скрипт для обработки данных')

# Добавляем аргументы
parser.add_argument('--items', nargs='+', help='Название файлов')
parser.add_argument('--report', type=str, help='Название отчетов')

# Парсим аргументы
args = parser.parse_args()

print(f"Обрабатываемые файлы: {args.items}")
print(f"Результат сохраняем в: {args.report}")
