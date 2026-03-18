# Test_task_workmate

# Создаем новое виртуальное окружение
python -m venv venv


# Активируем его (Windows)
venv\Scripts\activate

При ошибке ".venv\Scripts\activate : Невозможно загрузить файл ...\.venv\Scripts\Activate.ps1, так как выполнение сценариев отключено в этой системе."
Выполнить команду: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt

# Запустить один из вариантов скрипта парметр --output дает возможность выгрузить отчет в txt
python main.py --files resourses/math.csv resourses/programming.csv resourses/physics.csv  --output report.txt

# Для запуска тестов запустить
pytest -vv  

# Для проверки покрытия тестов
pytest --cov=scripts tests/