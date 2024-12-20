class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = self.is_valid_vin(__vin)
        self.__numbers = self.is_valid_numbers(__numbers)

    def is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber("Неверный тип vin номера")

        if vin < 1000000 or vin > 99999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")

        return vin

    def is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")

        if len(str(numbers)) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")

        return numbers


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car("Model1", 1000000, "f123dj")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")

try:
    second = Car("Model2", 300, "т001тр")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{second.model} успешно создан")

try:
    third = Car("Model3", 2020202, "нет номера")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{third.model} успешно создан")
