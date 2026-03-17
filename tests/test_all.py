import pytest
from scripts.stat_calculation import (get_median_coffe_report,
                                      get_mean_coffe_report,
                                      get_mode_coffe_report)
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
