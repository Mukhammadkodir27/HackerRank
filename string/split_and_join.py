# split and join string
#! Example 1
def split_and_join(line):
    return "-".join(line)
    
if __name__ == '__main__':
    line = input().split()
    result = split_and_join(line)
    print(result)

#! Example 2
def split_and_join(line):
    return "-".join(line.split())
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#! Example 3
def split_and_join(line):
    line = line.split()
    return "-".join(line)
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# if it was "".join(string) then it would result in #StrStrStr
# if it was " ".join(string) then: #Str Str Str
# now it is "-".join(string) so result is: Str-Str-Str
# str.split() is used to create sublists of a string, for example if input is "Hello my friend!"
# it will make it ["Hello", "my", "friend!"] because it is seperated via delimeter whitespace
# if there was input and with delimeter comma then, "Hello, my, friend"
# str.split(,) and it would create substrings or sublists of comma separated elements
