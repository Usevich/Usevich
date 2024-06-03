from datetime import datetime


class SuperDate(datetime):
    # Создаем словарь с месяцами
    SEASONS = {
        1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
        6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn',
        11: 'Autumn', 12: 'Winter'
    }
    # Создаем словарь с временами дня

    TIMES_OF_DAY = {
        'Night': range(0, 6),
        'Morning': range(6, 12),
        'Day': range(12, 18),
        'Evening': range(18, 24)
    }

    def get_season(self):
        return self.SEASONS[self.month] #Возвращаем месяц

    def get_time_of_day(self):
        for time_period, hours in self.TIMES_OF_DAY.items():
            if self.hour in hours:
                return time_period #Возвращаем время дня
        return "Unknown"


# Пример использования:
a = SuperDate(2024, 2, 22, 12)
print(a.get_season())  # Вывод: Winter
print(a.get_time_of_day())  # Вывод: Day