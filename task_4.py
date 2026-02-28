import logging

LOG_FILENAME = 'resourse/calculator.log'

logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format='[%(asctime)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def show_last_operations():
    try:
        with open(LOG_FILENAME, 'r') as file:
            lines = file.readlines()
            print("\nПоследние 5 операций:")
            for line in lines[-5:]:
                print(line.strip())
    except FileNotFoundError:
        print("\nЛог-файл ещё не создан. Выполните хотя бы одну операцию.")


def clear_log():
    open(LOG_FILENAME, 'w').close()
    print("Лог-файл очищен.\n")

print("*" * 15, "Калькулятор", "*" * 15)
print("Введите 'g' для очистки лог-файла или 'exit' для выхода.")

show_last_operations()

while True:
    s = input("Знак (+, -, *, /): ")
    if s == "exit":
        print("До свидания!")
        break
    if s == "g":
        clear_log()
        continue
    if s in ("+", "-", "*", "/"):
        try:
            x = float(input("x = "))
            y = float(input("y = "))
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if s == "+":
            result = x + y
        elif s == "-":
            result = x - y
        elif s == "*":
            result = x * y
        elif s == "/":
            if y != 0:
                result = x / y
            else:
                print("Деление на ноль!")
                continue

        print(f"Результат: {result:.2f}")

        log_message = f"{x} {s} {y} = {result}"
        logging.info(log_message)
    else:
        print("Неверный знак операции")