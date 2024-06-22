# Infinite Iterators
#! count()
# from itertools import count


# def count_example(start, step):
#     counter = count(start, step)
#     for c in counter:
#         print(c)
#         if c == 100:
#             break


# count_example(10, 5)

#! repeat()
# from itertools import repeat


# def repeat_example(element, max_repeats):
#     repeater = repeat(element, max_repeats)
#     for val in repeater:
#         print(val)


# repeat_example("Hello", 10)


#! cycle()
from itertools import cycle


def cycle_example(elements):
    i = 0
    cycler = cycle(elements)
    while i < 100:
        print(next(cycler), end=" ")
        i += 1


cycle_example("ABCD")
