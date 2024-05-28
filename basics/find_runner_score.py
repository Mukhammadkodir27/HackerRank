if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_elements = set()
    for i in arr:
        unique_elements.add(i)
    
    unique_elements.remove(max(unique_elements))
    print(max(unique_elements))

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.
