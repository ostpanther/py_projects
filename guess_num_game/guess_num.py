import random

# слова-выход
EXIT_WORDS = {"quit", "exit", "сдаюсь", "выход"}


def print_introduction():
    # "Распечатать вводное сообщение."
    print("\nЯ загадал число от 0 до 100. Попробуй угадать его.")


def print_less(num):
    # "Распечатать ответ на слишком большое число."
    print(f"SECRET_NUMBER < {num}. Твоё число больше.")


def print_greater(num):
    # "Распечатать ответ на слишком маленькое число."
    print(f"SECRET_NUMBER > {num}. Твоё число меньше.")


def print_equal(num):
    # "Распечатать ответ на угаданное число."
    print(f"SECRET_NUMBER = {num}. Ура!!! Ты угадал!")


def print_early_exit():
    # "Распечатать ответ на одно из EXIT_WORDS."
    print("Неужели ты сдался...")


def print_end():
    # "Распечатать сообщение об исчерпании количества попыток."
    print("Ты превысил лимит. Игра окончена")


def print_error(what):
    # "Человек, я тебя не понимаю!"
    quoted_exit_words = (f"'{w}'" for w in EXIT_WORDS)
    joined_exit_words = ", ".join(quoted_exit_words)
    print(f"Что такое '{what}'? Введи число или стоп-слово {joined_exit_words}.\n")


def main():
    # создал функцию-счетчик попыток с правильными окончаниями
    def counter_left():
        if COUNTER % 10 == 1:
            print("У вас осталось", COUNTER, "попытка\n")
        elif 2 <= (COUNTER % 10) <= 4:
            print("У вас осталось", COUNTER, "попытки\n")
        else:
            print("У вас осталось", COUNTER, "попыток\n")

    # Аннотация к игре__________________________

    print("Добро пожаловать в Угадайку!")
    input('Чтобы перейти к следующему шагу нажмите "Enter"')

    name = input("Введите ваше имя ниже\n")

    print("Приятно познакомиться,", name, "\n")
    print(
        "Правила игры просты:\n- программа загадывает число-секрет и предлагает игроку угадать его\n- игрок пытается угадать число или сдаётся.\n"
    )
    input(
        'Если ты захочешь прервать игру то введи одно из следующих слов:\n"quit", "exit", "сдаюсь", "выход"\n'
    )
    input("Начнем?")

    # Начало игры________________________________

    print_introduction()

    SECRET_NUMBER = random.randint(1, 100)

    num = input("\nВаше число: ")
    COUNTER = 9

    for i in range(COUNTER + 1):
        if num.isnumeric():
            num = int(num)
            if num == SECRET_NUMBER:
                print_equal(num)
                break
            if COUNTER != 0:
                if num > SECRET_NUMBER:
                    print_less(num)
                    counter_left()
                elif num < SECRET_NUMBER:
                    print_greater(num)
                    counter_left()
                COUNTER -= 1
                num = input("Введите число: ")
            else:
                print_end()
        elif num in EXIT_WORDS:
            print_early_exit()
            exit()
        else:
            print_error(num)
            num = input("Введите число: ")


if __name__ == "__main__":
    main()
# Не решено
# отсутствуют

# Решено
# лимит соблюдает
# написать сколько кол-во попыток осталось с окончаниями
# после ввода правльного числа делает break и не учитывает счетчик
# после 10 попыток прощается
# принимает слово-выход
# принимает аброкадабру
# на 10ой попытке правльного ответа принимает его
