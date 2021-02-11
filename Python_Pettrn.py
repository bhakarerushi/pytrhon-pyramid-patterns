
# half pyramid pattern of descending numbers.


n = int(input("enter no:"))

for i in range(n,0,-1):

    for j in range(i):

        print(i,end = " ")
    print(" ")


'''
enter no:5
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

'''
