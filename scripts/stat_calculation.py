from statistics import median, mean, mode


def get_median_coffe_report(students_dict: dict) -> list:

    med_report = []
    for name in students_dict:
        med_report.append([name, median(students_dict[name])])

    return med_report


def get_mean_coffe_report(students_dict: dict) -> list:

    mean_report = []
    for name in students_dict:
        mean_report.append([name, mean(students_dict[name])])

    return mean_report


def get_mode_coffe_report(students_dict: dict) -> list:

    mode_report = []
    for name in students_dict:
        mode_report.append([name, mode(students_dict[name])])

    return mode_report
