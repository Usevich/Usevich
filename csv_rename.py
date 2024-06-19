import csv


def write_holiday_cities(first_letter):
    visited_cities = set()
    wished_cities = set()

    with open('travel-notes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, visited, wished = row[0], row[1], row[2]
            if name.startswith(first_letter):  # Filter by first letter
                visited_cities.update(visited.split(';'))
                wished_cities.update(wished.split(';'))

    never_been_cities = wished_cities - visited_cities
    next_city = sorted(never_been_cities)[0] if never_been_cities else None

    # Sorting data for output
    visited_cities = sorted(visited_cities)
    wished_cities = sorted(wished_cities)
    never_been_cities = sorted(never_been_cities)

    with open('holiday.csv', 'w', newline='') as csvfile:
        fieldnames = ['Посетили', 'Хотят посетить', 'Никогда не были в', 'Следующим городом будет']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({
            'Посетили': ', '.join(visited_cities),
            'Хотят посетить': ', '.join(wished_cities),
            'Никогда не были в': ', '.join(never_been_cities),
            'Следующим городом будет': next_city if next_city else ''
        })


# Пример запуска с буквой "L"
write_holiday_cities('L')