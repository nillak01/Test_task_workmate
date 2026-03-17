import csv
from collections import defaultdict
from scripts.logger import logging


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
