
# unique pyramid patterns of digits.

n = int(input("enter no:"))


for i in range(1,n+1):

    for j in range(1,i):

        print(j, end = ' ')
    
    for j in range(i,0,-1):

        print(j, end = ' ' )

    print(' ')


'''

enter no:5
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

'''