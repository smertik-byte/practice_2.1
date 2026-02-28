students = [
'Иванов Иван: 5,4,3,5',
'Петров Петр: 4,3,4,4',
'Сидорова Мария: 5,5,5,5'
]
result_students = []

with open("resourse/students.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
for line in students:
    name, valution_str = line.strip().split(':')
    valution = list(map(int, valution_str.split(',')))
    mid = sum(valution) / len(valution)
    result_students.append((name, valution, mid))

with open('resourse/students.txt', 'w', encoding='utf-8') as outfile:
    for student in result_students:
        if student[2] > 4.0:
            outfile.write(f"{student[0]}: {', '.join(map(str, student[1]))}\n")
top_student = max(result_students, key=lambda x: x[2])
print(f"Лучший студент: {top_student[0]} со средним баллом {top_student[2]:.2f}")