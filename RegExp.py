import re


def extract_image_links(html_text):
    # Тут конечно подсмотрел в интернете
    #image_url_pattern = re.compile(r'<img\s+[^>]*src="(http?://[^">]+\.(?:jpg|jpeg|png|gif))"', re.IGNORECASE) #Так ничего не работает так как кавычки не те.
    image_url_pattern = re.compile(r'<img\s+[^>]*src=[\'"](https?://[^\'">]+\.(?:jpg|jpeg|png|gif))[\'"]',
                                   re.IGNORECASE) #А так ищес в двумя типами кавычек
    # Ищем совпадения
    image_links = image_url_pattern.findall(html_text)

    # Вохвращаем совпадения
    return image_links


# Пример использования функции
sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>")

image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")