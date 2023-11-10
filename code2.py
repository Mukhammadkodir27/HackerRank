if __name__ == '__main__':
    # Input the number of students
    n = int(input())

    # Create a nested list to store names and grades
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    second_lowest_grade = sorted(set([score for name, score in students]))[1]

    # Get names of students with the second lowest grade, sorted alphabetically
    result_names = sorted(
        [name for name, score in students if score == second_lowest_grade])

    # Print the names
    for name in result_names:
        print(name)


"""
records = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    records.append([name, score])

print(records)

sorted_records = list(sorted(records))

second_lowest_value = sorted_records[1]

second_lowest_indices = [i for i, x in enumerate(
    sorted_records) if x == second_lowest_value]

second_lowest_occurances = [(i, sorted_records[i])
                            for i in second_lowest_indices]


if second_lowest_occurances > 1:
    print(second_lowest_occurances)
else:
    print(second_lowest_value)
"""
