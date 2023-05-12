# Estudia como puedas
# Minimize waiting time.

def study_waiting_time(courses_study_times):
    waiting_time = 0
    courses_study_times.sort()
    remaining_courses = len(courses_study_times)
    for course in courses_study_times:
        waiting_time += course * remaining_courses
        remaining_courses += -1
    return waiting_time


def main():
    courses_amount, evaluations_amount = map(int, input().strip().split())

    courses_study_times = [0] * courses_amount
    for course in range(courses_amount):
        code, courses_study_times[course] = map(int, input().strip().split())

    evaluation_study_times = [0] * evaluations_amount
    for evaluation in range(evaluations_amount):
        evaluation_study_times[evaluation] = int(input().strip())

    waiting_time = study_waiting_time(courses_study_times)

    for evaluation in range(evaluations_amount):
        if evaluation_study_times[evaluation] >= waiting_time:
            print("APROBADO")
        else:
            print("SUSPENSO")


if __name__ == "__main__":
    main()
