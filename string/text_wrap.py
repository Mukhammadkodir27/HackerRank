import textwrap


def wrap(string, max_width):
    st = textwrap.fill(string, max_width)
    return st


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#! textwrap

"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

"""
