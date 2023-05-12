# Examen Jedi - Gonzalo Ortega
import math


def knapsack(students, remaining_force):
    knowledge = 0
    spent_force = 0
    best_students = []

    for ratio, student_id, value, cost in students:
        if cost <= remaining_force:
            knowledge += value
            spent_force += cost
            remaining_force -= cost
            if len(best_students) < 3:
                best_students.append(student_id)
        else:
            knowledge += ratio * remaining_force
            if len(best_students) < 3:
                best_students.append(student_id)
            return knowledge, spent_force, best_students

    return knowledge, spent_force, best_students


def main():
    student_amount = int(input().strip())
    students = []
    for _ in range(student_amount):
        student_id, value, cost = map(int, input().strip().split())
        ratio = value / cost
        students.append((ratio, student_id, value, cost))
    students.sort(reverse=True)

    force = int(input().strip())

    knowledge, spent_force, best_students = knapsack(students, force)

    print(str(math.ceil(knowledge)) + ' ' + str(spent_force))
    for student in best_students:
        print(student)


if __name__ == '__main__':
    main()
