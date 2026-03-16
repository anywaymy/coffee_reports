import argparse

from tabulate import tabulate

from reports import REPORT_MAPPING


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs="+", required=True, help="Пути к csv")
    parser.add_argument('--report', required=True, help="Тип отчёта (то что у нас в маппинге - median-coffee)")

    args = parser.parse_args()

    try:
        report_func = REPORT_MAPPING[args.report]
        data = report_func(args.files)

        headers = ["Студете", "Медиана трат на кофе"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
    except Exception as e:
        print(f"Ошибка отчёта: {e}")


if __name__ == "__main__":
    main()
