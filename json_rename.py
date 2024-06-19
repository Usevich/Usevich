# -*- coding: utf-8 -*-
import json
import os


def employees_rewrite(sort_type):
    try:
        # Приводим ключ для сортировки к нижнему регистру
        sort_type = sort_type.strip().lower()

        # Читаем данные из файла
        with open('employees.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Преобразуем ключи нижнему регистру чтобы было одинаково с ключем сортировки
        employees = [
            {k.lower(): v for k, v in employee.items()}
            for employee in data.get('employees', [])
        ]

        # Проверяем наличие ключа в словаре, если нету то выбрасываем исключение
        if not employees or sort_type not in employees[0]:
            raise ValueError('Bad key for sorting')

        # Сортируем данные
        if isinstance(employees[0][sort_type], str):
            sorted_data = sorted(employees, key=lambda x: x[sort_type])
        elif isinstance(employees[0][sort_type], (int, float)):
            # Зарплату сортируем по убыванию
            sorted_data = sorted(employees, key=lambda x: x[sort_type], reverse=True)
        else:
            raise ValueError('Unsupported data type for sorting')

        # Сохраняем отсортированные данные в новый файл
        sorted_filename = f'employees_{sort_type}_sorted.json'
        with open(sorted_filename, 'w', encoding='utf-8') as file:
            json.dump({"employees": sorted_data}, file, indent=4)

        print(f'Successfully sorted and saved to {sorted_filename}')
    #Дальше проверяем на стандвртные ошибки
    except FileNotFoundError:
        print("The file 'employees.json' does not exist.")
    except json.JSONDecodeError:
        print("Could not decode JSON from the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Пример вызова функции
employees_rewrite('firstName')
employees_rewrite('lastname')
employees_rewrite('department')
employees_rewrite('salary')
employees_rewrite('first_Name')