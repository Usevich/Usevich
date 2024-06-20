# -*- coding: utf-8 -*-
import cv2
import numpy as np

# Создаем изображение размером 500x500 пикселей с 3 цветовыми каналами
size = 500
image = np.zeros((size, size, 3), dtype=np.uint8)

# Зададим цвета
white = (255, 255, 255)
blue = (255, 128, 0)
green = (0, 255, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)
#Линиями создаем градиент фона
for i in range(size):
    color = (
        int(255 * (i / size)), # тут можно поиграться отткнками градиента
        int(255 * (1 - i / size)),
        128
    )
    cv2.line(image, (i, 0), (i, size), color, 1)

# Рисуем круг
center = (size // 2, size // 2)
radius = 200
cv2.circle(image, center, radius, white, 3)

# Рисуем полукруг через эллипсс одинаковыми осями
center = (size // 2, size // 2)
axes = (50, 50)
angle = 0
start_angle = 0
end_angle = 180
cv2.ellipse(image, center, axes, angle, start_angle, end_angle, green, 3)
# Уменьаем оси и рисуем второй
axes = (25, 25)
cv2.ellipse(image, center, axes, angle, start_angle, end_angle, green, 3)

# Рисуем первую линию
start_point = (size // 2 - 50, size // 2)
end_point = (size // 2 - 50, size // 2 - 50)
cv2.line(image, start_point, end_point, blue, thickness=3)
# Сдвигая Рисуем следущюю линию
start_point = (size // 2 - 25, size // 2)
end_point = (size // 2 - 25, size // 2 - 50)
cv2.line(image, start_point, end_point, blue, thickness=3)
# Сдвигая Рисуем следущюю линию
start_point = (size // 2 + 25, size // 2)
end_point = (size // 2 + 25, size // 2 - 50)
cv2.line(image, start_point, end_point, blue, thickness=3)
# Сдвигая Рисуем следущюю линию
start_point = (size // 2 + 50, size // 2)
end_point = (size // 2 + 50, size // 2 - 50)
cv2.line(image, start_point, end_point, blue, thickness=3)
# И наконец две горизонтальных линии
start_point = (size // 2 - 50, size // 2 - 50)
end_point = (size // 2 - 25, size // 2 - 50)
cv2.line(image, start_point, end_point, red, thickness=3)
# Вторая
start_point = (size // 2 + 50, size // 2 - 50)
end_point = (size // 2 + 25, size // 2 - 50)
cv2.line(image, start_point, end_point, red, thickness=3)


# Отображаем изображение
cv2.imshow("U Letter", image)
cv2.waitKey(0)  # Ждем нажатия любой клавиши
cv2.destroyAllWindows() # Уничтожаем окно