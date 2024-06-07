def average(array):
    array_to_set = set(array)
    total = sum(array_to_set)
    amount = len(array_to_set)
    return total / amount


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
