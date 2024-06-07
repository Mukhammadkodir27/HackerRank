if __name__ == "__main__":
    m = int(input())
    M = list(map(int, input().split()))
    n = int(input())
    N = list(map(int, input().split()))

    A = set(M)
    B = set(N)

    set_union = A.union(B)
    print(len(set_union))
