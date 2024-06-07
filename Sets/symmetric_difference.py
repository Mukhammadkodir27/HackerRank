if __name__ == "__main__":
    m = int(input())
    M = list(map(int, input().split()))
    n = int(input())
    N = list(map(int, input().split()))

    A = set(M)
    B = set(N)

    difference = A.symmetric_difference(B)
    sorted_set = sorted(difference, reverse=False)
    for i in sorted_set:
        print(i)
