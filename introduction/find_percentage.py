if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0.00
    selected = student_marks[query_name]
    for select in selected:
        total = total + select

    result = total / 3

    print(f"{result:.2f}")
