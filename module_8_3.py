class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.messCar = message


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.messVin = message


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.__vin = __vin
        if self._is_valid_numbers(__numbers):
            self.__numbers = __numbers

    def __is_valid_vin(vin_number):
        if isinstance(vin_number, int):
            if vin_number < 10000000 and vin_number > 999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номера')

            
    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.messCar)
except IncorrectCarNumbers as exc:
    print(exc.messVin)
else:
    print(f'{first.model} успешно создан')