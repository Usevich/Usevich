import logging
import requests as rq

#Настройка логгеров
success_logger = logging.getLogger('success_responses')
success_logger.setLevel(logging.INFO) # Иначе не пишется в лог, можно поставить DEBUG
bad_responses_logger = logging.getLogger('bad_responses')
blocked_responses_logger = logging.getLogger('blocked_responses')

#Форматирование лог-сообщений
formatter = logging.Formatter('%(levelname)s: %(message)s')

# Обработчики логов
success_file_handler = logging.FileHandler('success_responses.log')
bad_responses_file_handler = logging.FileHandler('bad_responses.log')
blocked_responses_file_handler = logging.FileHandler('blocked_responses.log')

# Добавление форматеров и обработчиков к логгерам
success_logger.addHandler(success_file_handler)
bad_responses_logger.addHandler(bad_responses_file_handler)
blocked_responses_logger.addHandler(blocked_responses_file_handler)

success_file_handler.setFormatter(formatter)
bad_responses_file_handler.setFormatter(formatter)
blocked_responses_file_handler.setFormatter(formatter)

# Список сайтов
sites = [
    'https://www.youtube.com/',
    'https://wikipedia.org',
    'https://yahoo.com',
    'https://yandex.ru',
    'https://whatsapp.com',
    'https://amazon.com',
    'https://www.ozon.ru',
    'https://instagram.com',
    'https://twitter.com',
]

# Проверка доступности сайтов
for site in sites:
    try:
        response = rq.get(site, timeout=3)

        if response.status_code == 200:
            success_logger.info(f'{site}, response - {response.status_code}')
        else:
            bad_responses_logger.warning(f'{site}, response - {response.status_code}')

    except rq.exceptions.ConnectionError:
        blocked_responses_logger.error(f'{site}, NO CONNECTION')
    except (rq.exceptions.Timeout, rq.exceptions.HTTPError) as e:
        bad_responses_logger.error(f'{site}, response - {e}')

