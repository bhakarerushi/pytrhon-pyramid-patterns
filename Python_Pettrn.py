
# inverted half pyramid of numbers starting with 0.

n = int(input("enter no:"))

for i in range(n,0,-1):

    for j in range(i+1):

        print(j,end = ' ')

    print(" ")


'''

enter no:5
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1

'''