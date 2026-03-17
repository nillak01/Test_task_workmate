from stat_calculation import (get_median_coffe_report, get_mean_coffe_report,
                              get_mode_coffe_report)
from parser import get_pars
from processing_csv import read_csv
from cli import show_table


def run():

    reports_dict = {
        'median-coffee': get_median_coffe_report,
        'mean-coffee': get_mean_coffe_report,
        'mode-coffee': get_mode_coffe_report,
    }

    args = get_pars()
    # Задаем название для отчета по умолчанию
    report_name = args.report if args.report else 'median-coffee'
    # Заголовки столбцов для вывода
    headers = ["student", report_name]
    students_dict = read_csv(args.files)
    data = reports_dict[report_name](students_dict)
    show_table(data, headers)
