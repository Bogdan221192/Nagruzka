import json
tests_file = input('Введите путь к файлу tests.json')
values_file = input('Введите путь к файлу values.json')
report_file = input('Введите путь к файлу report.json')

def update_values(tests_data, values_map):
    for entry in tests_data:
        entry_id = entry.get('id')
        if entry_id in values_map:
            entry['value'] = values_map[entry_id]
        if 'values' in entry and isinstance(entry['values'], list):
            update_values(entry['values'], values_map)
        elif 'tests' in entry and isinstance(entry['tests'], list):
            update_values(entry['tests'], values_map)


def generate_report(tests_file='tests.json', values_file='values.json', report_file='report.json'):

    try:
        with open(tests_file, 'r') as f:
            tests_data = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: {tests_file} не найден.")
        return

    # 2. Load data from values.json
    try:
        with open(values_file, 'r') as f:
            values_data = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: {values_file} не найден.")
        return

    values_map = {}
    if 'values' in values_data and isinstance(values_data['values'], list):
        for item in values_data['values']:
            if 'id' in item and 'value' in item:
                values_map[item['id']] = item['value']

    if 'tests' in tests_data and isinstance(tests_data['tests'], list):
        update_values(tests_data['tests'], values_map)
    else:
        update_values(tests_data, values_map)

    try:
        with open(report_file, 'w') as f:
            json.dump(tests_data, f, indent=2)
        print(f"Успешно создан файл отчета '{report_file}'")
    except IOError as e:
        print(f"Ошибка записи в файл {report_file}: {e}")

if __name__ == "__main__":
    generate_report()