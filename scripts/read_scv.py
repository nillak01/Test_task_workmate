import csv

def check_is_path(paths: list):
    try:
        pass
    except Exception as e:
    # Что делать, если произошла ошибка
        print(f"Произошла ошибка: {e}")


def read_csv(paths: list):
    # Чтение с заголовками (как словарь)
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['Имя'], row['Возраст'])  # Доступ по имени колонки