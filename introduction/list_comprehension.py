if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coordinates = [[i, j, k] for i in range(
        x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

    print(coordinates)

"""
et's learn about list comprehensions! You are given three integers  and  
representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by 
on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions 
rather than multiple loops, as a learning exercise.

Example
All permutations of  are:
.
Print an array of the elements that do not sum to .
Input Format
Four integers  and , each on a separate line.
Constraints
Print the list in lexicographic increasing order.
Sample Input 0

1
1
1
2
Sample Output 0

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
Explanation 0

Each variable  and  will have values of  or . All permutations of lists in the form .
Remove all arrays that sum to  to leave only the valid permutations.

"""


"""
The range(z + 1) (as well as range(x + 1) and range(y + 1)) comes from the need to include the endpoint value in our iteration. Here's a detailed explanation:

Understanding range()
The range(start, stop) function in Python generates a sequence of numbers starting from start up to but not including stop. By default, start is 0 if not specified. Therefore, range(stop) is equivalent to range(0, stop).

Why range(x + 1), range(y + 1), and range(z + 1)?
Given the problem statement, you need to generate all possible coordinates [i, j, k] where:

0
≤
𝑖
≤
𝑥
0≤i≤x
0
≤
𝑗
≤
𝑦
0≤j≤y
0
≤
𝑘
≤
𝑧
0≤k≤z
Including the End Value
If you use range(x), range(y), or range(z), the highest value in the range would be x-1, y-1, and z-1, respectively. This would exclude the values x, y, and z themselves, which is not what we want. Instead, we need to include these values.

Example:
If x = 1, using range(x) would give range(1), which generates the sequence [0]. It does not include 1.

By using range(x + 1), we generate the sequence [0, 1], which includes all values from 0 to x.

Code Breakdown
Here’s the relevant part of the code again:

python
Copy code
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
range(x + 1): Generates numbers from 0 to x inclusive.
range(y + 1): Generates numbers from 0 to y inclusive.
range(z + 1): Generates numbers from 0 to z inclusive.
This ensures that i, j, and k each take on every possible value from 0 to their respective upper limits.

Complete Code
Putting it all together ensures we get all possible coordinates where i, j, and k range from 0 to x, y, and z respectively, and then we filter out those whose sum equals n:

python
Copy code
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    
    print(coordinates)
This will correctly generate and print the list of coordinates, including all valid values from 0 to the specified limits.

"""
