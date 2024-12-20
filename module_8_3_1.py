class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if isinstance(__vin, int):
            if __vin < 10000000 and __vin > 999999:
                self.__vin = __vin
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            raise IncorrectVinNumber('Некорректный тип vin номера')


        #if self._is_valid_numbers(__numbers):
        if isinstance(__numbers, str):
            if len(__numbers) == 6:
                self.__numbers = __numbers
            else:
                raise IncorrectCarNumbers('Неверная длина номера')
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')


    # def __is_valid_vin(vin_number):
    #     if isinstance(vin_number, int):
    #         if vin_number < 10000000 and vin_number > 999999:
    #             return True
    #         else:
    #             raise IncorrectVinNumber('Неверный диапазон для vin номера')
    #     else:
    #         raise IncorrectVinNumber('Некорректный тип vin номера')

    # def __is_valid_numbers(numbers):
    #     if not isinstance(numbers, str):
    #         raise IncorrectCarNumbers('Некорректный тип данных для номеров')
    #     if len(numbers) != 6:
    #         raise IncorrectCarNumbers('Неверная длина номера')
    #
    #     return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')


try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')