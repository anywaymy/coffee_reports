import argparse

from tabulate import tabulate

from reports import REPORT_MAPPING


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs="+", required=True, help="Пути к csv")
    parser.add_argument('--report', required=True, help="Тип отчёта (то что у нас в маппинге - median-coffee)")

    args = parser.parse_args()

    if args.report not in REPORT_MAPPING:
        print(f"Отчёт {args.report} не найден. Вам доступны - {list(REPORT_MAPPING)}")

    report_func = REPORT_MAPPING[args.report]
    data = report_func(args.files)

    headers = ["Студете", "Медиана трат на кофе"]
    print(tabulate(data, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
