if __name__ == "__main__":
    N = int(input())
    arr = []

    for i in range(N):
        command = input()
        parts = command.split()

        if parts[0] == "insert":
            arr.insert(int(parts[1]), int(parts[2]))
        elif parts[0] == "print":
            print(arr)
        elif parts[0] == "remove":
            arr.remove(int(parts[1]))
        elif parts[0] == "append":
            arr.append(int(parts[1]))
        elif parts[0] == "sort":
            arr.sort()
        elif parts[0] == "pop":
            arr.pop()
        elif parts[0] == "reverse":
            arr.reverse()


# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example
# : Append  to the list, .
# : Append  to the list, .
# : Insert  at index , .
# : Print the array.
# Output:


# method

if __name__ == "__main__":
    arr = []
    n = int(input())  # number of commands

    for i in range(n):
        command_input = input()
        command_list = command_input.split()
        command = command_list[0]

        if command == "insert":
            # in insert we need to provide 2 args, index and value
            arr.insert(int(command_list[1]), int(command_list[2]))
        elif command == "print":
            print(arr)
        elif command == "remove":
            # command[0] was command name and command[1] is its value (element)
            arr.remove(int(command_list[1]))
        elif command == "append":
            arr.append(int(command_list[1]))
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()

