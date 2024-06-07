if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))

    amount = int(input())
    for i in range(amount):
        command = input().split()

        #! here i forgot to write int(command[1]) as a result it gave runtime error
        #! dont forget to converst input string to int or else there will be an error!
        if command[0] == "pop":
            s.pop()
        elif command[0] == "discard":
            s.discard(int(command[1]))
        elif command[0] == "remove":
            s.remove(int(command[1]))
    # i did not read carefully the instructions, as a result i wrote len() instead of sum()
    print(sum(s))
