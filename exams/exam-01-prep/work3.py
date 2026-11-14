# Парковка торгового центра печатает подтверждение брони.
# Вводятся название парковки, номер этажа, номер первого места, число мест и цена одного места за день — все числа целые.
# Места идут подряд. Выведите две строки, как в примерах, с помощью f-строк.
# Номер последнего места и сумму к оплате посчитайте выражениями прямо в фигурных скобках.

NameParking = (input("Название парковки: "))
numberfloor = int(input("номер этажа: "))
OneNumber = int(input("номер первого места: "))
numberplace = int(input("количество мест: "))
price = int(input("цена одного места за день: "))

NameParkingEnd = "<" + NameParking + ">"
parkingplace = OneNumber + numberplace - 1
priceplace = price * numberplace

print(f"{NameParkingEnd}, этаж {numberfloor}, места с {OneNumber} по {parkingplace}")
print(f"{numberplace} шт. по {price} руб ., к оплате: {priceplace} руб.")

#я не понял где стрелочки на клавиатуре