import json
import csv

# Читаем JSON-файл
with open('data//Amsterdam24.09.06.json', 'r') as json_file:
    data = json.load(json_file)

# Открываем CSV-файл для записи

with open('weather_data.csv', 'w', newline='') as csv_file:
    # Создаем объект writer для записи в CSV-файл
    writer = csv.writer(csv_file)

    # Записываем заголовок в CSV-файл
    writer.writerow(['Hour', 'Feels Like', 'Condition'])

    # Перебираем данные по часам
    for hour in data['forecasts'][0]['hours']:
        # Записываем данные в CSV-файл
        writer.writerow([hour['hour'], hour['feels_like'], hour['condition']])