# split and join string

#! Example 1
def split_and_join(line):
    return "-".join(line)


if __name__ == '__main__':
    line = input().split()
    result = split_and_join(line)
    print(result)

#! Example 2


def split_and_join(line):
    return "-".join(line.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#! Example 3


def split_and_join(line):
    line = line.split()
    return "-".join(line)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
