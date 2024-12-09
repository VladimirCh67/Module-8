def  personal_sum(numbers):
    result = 0
    incor_dat = 0
    for i in range(len(numbers)):
        try:
            result += numbers[i]
        except TypeError as exc:
            incor_dat += 1
            print(exc, numbers[i])

    return (result, incor_dat)


def calculate_average(numbers):
    try:
        return personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


