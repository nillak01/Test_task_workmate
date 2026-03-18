import pytest
import logging
from scripts.stat_calculation import (get_median_coffe_report,
                                      get_mean_coffe_report,
                                      get_mode_coffe_report)
from scripts.cli import get_pars, process_cli_parser
from scripts.processing_csv import read_csv
from scripts.main_functions import run


@pytest.mark.parametrize("test_input,expected", [
    ({'Иванов И. И.': [200, 500, 600, 100]}, [['Иванов И. И.', 350.0]]),
    ({'Дарья Петрова': [200, 250, 300]}, [['Дарья Петрова', 250]]),
    ({'Елена Волкова': [280, 310, 340]}, [['Елена Волкова', 310]]),
    ({'Анна Белова': [280, 310, 340]}, [['Анна Белова', 310]]),
    ({'Краснов Олег': [0, 0, 0]}, [['Краснов Олег', 0]]),
    ({'Nguen Li': [0, 100, 200]},  [['Nguen Li', 100]])
    # тест на граничный случай
])
def test_calculate_median_parametrized(test_input, expected):
    assert get_median_coffe_report(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(
    {'Иванов И. И.': [200, 500, 600, 100],
     'Дарья Петрова': [200, 250, 300],
     'Елена Волкова': [280, 310, 340],
     'Анна Белова': [280, 310, 340],
     'Краснов Олег': [0, 0, 0],
     'Nguen Li': [0, 100, 200]},
    [['Иванов И. И.', 350.0],
     ['Дарья Петрова', 250],
     ['Елена Волкова', 310],
     ['Анна Белова', 310],
     ['Краснов Олег', 0],
     ['Nguen Li', 100]])]
    # тест на граничный случай
)
def test_calculate_mean_parametrized(test_input, expected):
    assert get_mean_coffe_report(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(
    {'Иванов И. И.': [201, 500, 602, 100],
     'Дарья Петрова': [400, 250, 300],
     'Дудец Артем': [500, 343, 800],
     'Анна Белова': [280, 310, 340],
     'Шматко Олег': [0, 1, 3],
     'Nguen Li': [0, 100, 205]},
    [['Иванов И. И.', 201],
     ['Дарья Петрова', 400],
     ['Дудец Артем', 500],
     ['Анна Белова', 280],
     ['Шматко Олег', 0],
     ['Nguen Li', 0]])]
    # тест на граничный случай
)
def test_calculate_moda_parametrized(test_input, expected):
    assert get_mode_coffe_report(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [(
    ['--files', 'resourses/math.csv'], [['resourses/math.csv'], None]),
    (['--files', 'resourses/math.csv', '--report', 'median-coffee'], [['resourses/math.csv'], 'median-coffee']),
    (['--files', 'resourses/math.csv', 'resourses/programming.csv', 'resourses/physics.csv'], [['resourses/math.csv', 'resourses/programming.csv', 'resourses/physics.csv'], None]),
    (['--files', 'resourses/math.c'], [['resourses/math.c'], None]),
    ([], [None, None])]
    # тест на граничный случай
)
def test_parse_positional_arg(test_input, expected):
        
        """Тест позиционного аргумента"""
        args = get_pars(test_input)
        assert args.files == expected[0]
        assert args.report == expected[1]


@pytest.mark.parametrize("test_input,expected", [(
    ['--files', 'resourses/math.csv',  '--report', 'mean-coffee'], {'files': ['resourses/math.csv'],
                                        'report': 'mean-coffee',
                                        'output': None}),
    (['--files', 'resourses/math.csv', '--report', 'median-coffee'], {'files': ['resourses/math.csv'],
                                        'report': 'median-coffee',
                                        'output': None}),
    (['--files', 'resourses/math.csv', 'resourses/programming.csv', 'resourses/physics.csv',  '--report', 'median-coffee'],{'files': ['resourses/math.csv', 'resourses/programming.csv', 'resourses/physics.csv'],
                                        'report': 'median-coffee',
                                        'output': None})]
    # тест на граничный случай
)
def test_process_positional_arg(test_input, expected):
        
        """Тест позиционного аргумента"""
        files, report_name, output = process_cli_parser(test_input)
        assert files == expected['files']
        assert report_name == expected['report']
        assert output == expected['output']


def test_process_positional_arg_2(caplog):
        
        """Тест позиционного аргумента"""
        caplog.set_level(logging.CRITICAL) # Говорим caplog перехватывать CRITICAL и выше

        # Ожидаем, что будет вызван SystemExit
        with pytest.raises(SystemExit) as exc_info:
            process_cli_parser([])
        
        # Проверяем код возврата
        assert exc_info.value.code == 1
        
        # Проверяем, что сообщение было залогировано
        assert "Критическая ошибка: не указан ни один файл" in caplog.text
        
        # Можно проверить уровень логирования
        critical_records = [r for r in caplog.records if r.levelname == 'CRITICAL']
        assert len(critical_records) == 1
    

def test_process_positional_arg_3(caplog):
    
    """Тест позиционного аргумента"""
    caplog.set_level(logging.WARNING) # Говорим caplog перехватывать CRITICAL и выше

    process_cli_parser(['--files', 'resourses/math.csv'])
    
    # Проверяем, что сообщение было залогировано
    assert "Report не указан. Название устанавливается по умолчанию median-coffee" in caplog.text
    
    # Можно проверить уровень логирования
    warning_records = [r for r in caplog.records if r.levelname == 'WARNING']
    assert len(warning_records) == 1


def test_process_csv(caplog):
    
    """Тест позиционного аргумента"""
    caplog.set_level(logging.WARNING) # Говорим caplog перехватывать CRITICAL и выше

    test_dct = read_csv(['resourses/math.cs', 'Биба', 'Боба'])
    
    # Проверяем, что сообщение было залогировано
    assert "Предупреждение: файл resourses/math.cs не найден" in caplog.text
    assert "Предупреждение: файл Биба не найден" in caplog.text
    assert "Предупреждение: файл Боба не найден" in caplog.text
    
    # Можно проверить уровень логирования
    warning_records = [r for r in caplog.records if r.levelname == 'WARNING']
    assert len(warning_records) == 3

    assert test_dct==dict()


def test_run(caplog):
        
        """Тест позиционного аргумента"""
        caplog.set_level(logging.CRITICAL) # Говорим caplog перехватывать CRITICAL и выше

        # Ожидаем, что будет вызван SystemExit
        with pytest.raises(SystemExit) as exc_info:
            run([])
        
        # Проверяем код возврата
        assert exc_info.value.code == 1
        
        # Проверяем, что сообщение было залогировано
        assert "Критическая ошибка: не указан ни один файл" in caplog.text
        
        # Можно проверить уровень логирования
        critical_records = [r for r in caplog.records if r.levelname == 'CRITICAL']
        assert len(critical_records) == 1
        