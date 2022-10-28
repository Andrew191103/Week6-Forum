eren = {
    "name": "Eren",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

mikasa = {
    "name": "Mikasa",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

armin = {
    "name": "Armin",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [eren, mikasa, armin]

for s in students:
    print(s["name"])
    print(s["homework"])
    print(s["quizzes"])
    print(s["tests"])


def average(numbers):
    total = float(sum(numbers))
    media = total / (len(numbers))
    return media


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    final = 0.1 * homework + 0.3 * quizzes + 0.6 * tests
    return final


def get_letter_grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    elif s >= 70:
        return "C"
    elif s >= 60:
        return "D"
    else:
        return "F"


def get_class_average(students):
    results = []
    for student in students:
        r = get_average(student)
        results.append(r)

    return average(results)


students = [eren, mikasa, armin]

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))