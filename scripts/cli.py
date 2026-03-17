from tabulate import tabulate


def show_table(data: list, headers: list):

    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)
