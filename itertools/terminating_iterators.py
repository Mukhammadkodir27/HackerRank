# Terminating Iterators

#! accumulate()

# from itertools import accumulate


# def accumulate_example(elements):
#     running_sum = accumulate(elements)
#     print(list(running_sum))


# accumulate_example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

#! chain()

# from itertools import chain


# def chain_example(elements1, elements2):
#     chained = chain(elements1, elements2)
#     for chain_each in chained:
#         print(chain_each, end=" ")


# chain_example("ABC", "DEF")
# # A B C D E F

#! chain.from_iterable()
# from itertools import chain


# def chain_from_iterable_example(iterable):
#     chained = chain.from_iterable(iterable)
#     for chains in chained:
#         print(chains, end=" ")


# chain_from_iterable_example([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#! compress()

# from itertools import compress


# def compress_example(data, selectors):
#     compressed = compress(data, selectors)
#     print(list(compressed))


# compress_example([["a", "b", "c"], [1, 2, 3], [True, False, True]],
#                  [True, True, False])

# # so it is going to show 1 1 0, which means, data[0], data[1] will be shown and data[2] not or lets say compressed


#! pairwise()

from itertools import pairwise


def pairwise_example(iterable):
    paired = pairwise(iterable)
    print(list(paired))


pairwise_example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10)]
