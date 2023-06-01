#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

#Example
#
#: Append  to the list, .
#: Append  to the list, .
#: Insert  at index , .
#: Print the array.
#Output:
#[1, 3, 2]

N = int(input())

commands = {
    "insert": lambda x, y, z: x.insert(y, z),
    "print": lambda x: print(x),
    "remove": lambda x, y: x.remove(y),
    "append": lambda x, y: x.append(y),
    "sort": lambda x: x.sort(),
    "pop": lambda x: x.pop(),
    "reverse": lambda x: x.reverse(),
}
res = []
for i in range(N):        
    a = input()
    split_a = a.split(' ')
    command = split_a[0]
    try:
        commands[command](res, int(split_a[1]), int(split_a[2]))
    except IndexError:
        try:
            commands[command](res, int(split_a[1]))
        except IndexError:
            commands[command](res)

#Sample Input 0

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print
#Sample Output 0

#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]