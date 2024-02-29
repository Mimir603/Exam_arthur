"""
Игра "угадывай слово". Игра спрашивает число и сравнивает с загаданым числом. У вас 10 попыток.
"""
import random

GUESSED_MADE = 0

NUMBER = random.randint(1, 100)
print ('Я загадал число между 1 и 100. Сможешь угадать?')
try:
    while GUESSED_MADE < 10:
        GUESS = int(input('Введите число: '))
        GUESSED_MADE += 1
        if GUESS < NUMBER:
            print (f'Число {GUESS} меньше загаданного.')
        if GUESS > NUMBER:
            print (f'Число {GUESS} больше загаданного.')
        if GUESS == NUMBER:
            break
except ValueError:
    print("Введите число!")
except FloatingPointError:
    print("Введите целое число!")

if GUESS == NUMBER:
    print (f'Неверно! Ты угадал число, использовав {GUESSED_MADE} попыток!')
else:
    print (f'Неверно! Число оказалось {NUMBER}'.format(NUMBER))
