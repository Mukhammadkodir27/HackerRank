if __name__ == "__main__":
    N = int(input())
    countries = set()
    for n in range(N):
        country = input()
        countries.add(country)
    print(len(countries))
