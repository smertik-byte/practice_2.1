import csv

FILENAME = 'resourse/products.csv'

with open('resourse/products.csv', 'w', encoding='utf-8') as f:
    f.write('Название Цена Количество\n')
    f.write('Яблоки 100 50\n')
    f.write('Бананы 80 30\n')
    f.write('Молоко 120 20\n')
    f.write('Хлеб 40 100\n')
print("Файл создан.")

products = []

def read_products():
    try:
        with open(FILENAME, mode= 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, delimiter=' ')
            for row in reader:
                row['Цена'] = int(row['Цена'])
                row['Количество'] = int(row['Количество'])
                products.append(row)
        print("Данные успешно считаны")
    except FileNotFoundError:
        print(f"Файл {FILENAME} не найден. Начинаем с пустого списка.")
    return products

def save_products(products):
    with open(FILENAME, mode='w', encoding='windows-1251', newline='') as file:
        fieldnames = ['Название', 'Цена', 'Количество']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=' ')
        writer.writeheader()
        for p in products:
            writer.writerow(p)
    print("Данные успешно сохранены.")
products = read_products()
while True:
    print("\nВыберите действие:")
    print("1. Просмотр всех товаров")
    print("2. Добавить новый товар")
    print("3. Поиск товара по названию")
    print("4. Расчет общей стоимости товаров")
    print("5. Выйти и сохранить изменения")
    choice = input("Введите номер действия: ")
    if choice == '1':
        if products:
            print("\nТовары на складе:")
            for p in products:
                print(f"{p['Название']}: Цена={p['Цена']}, Количество={p['Количество']}")
        else:
            print("Склад пуст")
    elif choice == '2':
        name = input("Введите название товара: ")
        try:
            price = int(input("Введите цену: "))
            quantity = int(input("Введите количество: "))
            products.append({'Название': name, 'Цена': price, 'Количество': quantity})
            print(f"Товар '{name}' добавлен.")
        except ValueError:
            print("Ошибка ввода. Цена и количество должны быть числами.")
    elif choice == '3':
        search_name = input("Введите название для поиска: ")
        found = False
        for p in products:
            if p['Название'].lower() == search_name.lower():
                print(f"Найден товар: {p['Название']}, Цена={p['Цена']}, Количество={p['Количество']}")
                found = True
                break
        if not found:
            print("Товар не найден.")
    elif choice == '4':
        total_value = sum(p['Цена'] * p['Количество'] for p in products)
        print(f"Общая стоимость всех товаров: {total_value}")
    elif choice == '5':
        save_products(products)
        print("Работа завершена.")
        break
    else:
        print("Некорректный ввод, попробуйте ещё раз.")