# Test_task_workmate

# Создаем новое виртуальное окружение
python -m venv venv


# Активируем его (Windows)
venv\Scripts\activate

При ошибке .venv\Scripts\activate : Невозможно загрузить файл ...\.venv\Scripts\Activate.ps1, так как выполнение сценариев отключено в этой системе.
Выполнить команду: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Устанавливаем зависимости из requirements.txt
pip install -r requirements.txt
