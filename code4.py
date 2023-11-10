# N = int(input())

# while True:
#     try:
#         user_input = input()
#         values = tuple(map(int, user_input.split()))
#         if len(values) == N:
#             break
#         else:
#             print("Please enter exactly three values.")
#             exit()
#     except ValueError:
#         print("Invalid input. Please enter three integers separated by a space.")
#         exit()

# hash_value = hash(values)
# print(hash_value)

if __name__ == '__main__':
    n = int(input())  # Number of elements in the tuple
    # Create a tuple from input elements
    elements = tuple(map(int, input().split()))

    t = tuple(elements)

    print(hash(t))
