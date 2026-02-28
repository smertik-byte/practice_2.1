lines = [
    'Ревизор',
    'Герой нашего времени',
    'Великий Гэтсби',
    'Лолита',
    'Вино из одуванчиков'
]
with open("resourse/text.txt", "w", encoding="utf-8") as file:
    for i in lines:
        file.write(i + "\n")

def quanty_lines(filename):
    quanty = 0
    with open(filename) as file:
        for line in file:
            quanty += 1
    return quanty


def quanty_words(filename):
    quanty = 0
    with open(filename) as file:
        for line in file:
            words = line.strip().split()
            quanty += len(words)
    return quanty

def max_line(filename):
    with open(filename) as file:
        longest = max(file, key = len)
    return longest

print(f"\nКоличество строк в файле: "
      f"{quanty_lines("resourse/text.txt")}")
print(f"Количество слов в файле:"
      f" {quanty_words("resourse/text.txt")}")
print(f"Самая длинная строка:"
      f" {max_line("resourse/text.txt")}")