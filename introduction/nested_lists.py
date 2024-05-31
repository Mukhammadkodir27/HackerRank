if __name__ == '__main__':
    students = []
    for student in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    scores = []
    for student in students:
        scores.append(student[1])

    scores.sort()
    set_score = set(scores)
    second_lowest_grade = sorted(set_score)[1]
    second_lowest_names = []

    for student in students:
        if student[1] == second_lowest_grade:
            second_lowest_names.append(student[0])

    second_lowest_names.sort()

    for student in second_lowest_names:
        print(student)
