import csv
from collections import defaultdict
from statistics import median


def calculate_median_coffee(files):
    student_data = defaultdict(list)

    for file in files:
        with open(file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['student']
                spent = float(row['coffee_spent'])
                student_data[name].append(spent)

    report_data = []
    for student, costs in student_data.items():
        report_data.append([student, median(costs)])

    report_data.sort(key=lambda x: x[1], reverse=True)

    return report_data


REPORT_MAPPING = {
    'median-coffee': calculate_median_coffee
}
