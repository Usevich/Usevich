import inspect

def introspection_info(obj):


  result = {
      "Тип": type(obj),
      "Атрибуты": dir(obj),  #  имена атрибутов
      "Методы": [m for m in dir(obj) if callable(getattr(obj, m))],  # имеан методов
      "Модуль": inspect.getmodule(obj),  #Модуль, где определен объект
  }

  return result

# Пример использования
number_info = introspection_info(42)
string_info = introspection_info('Привет')
print(number_info)
print('===================================')

for key, value in string_info.items():
    print(key, value)