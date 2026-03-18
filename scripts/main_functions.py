from scripts.stat_calculation import (get_median_coffe_report,
                                      get_mean_coffe_report,
                                      get_mode_coffe_report)
from scripts.processing_csv import read_csv
from scripts.cli import process_cli_parser, show_table


def run(args=None):

    reports_dict = {
        'median-coffee': get_median_coffe_report,
        'mean-coffee': get_mean_coffe_report,
        'mode-coffee': get_mode_coffe_report,
        'another': get_median_coffe_report,
    }

    files, report_name, output = process_cli_parser(args)
    # Заголовки столбцов для вывода
    headers = ["student", report_name]
    students_dict = read_csv(files)
    try:
        reports_dict[report_name]
        data = reports_dict[report_name](students_dict)
    except Exception:
        data = reports_dict['another'](students_dict)
    show_table(data, headers, output)
