if __name__ == '__main__':
    n = int(input("n: "))
    arr = map(int, input().split())

    arr = sorted(arr)
    print(arr[len(arr)-3])
