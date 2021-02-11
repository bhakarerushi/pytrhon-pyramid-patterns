
# Even number pyramid pattern.

n = int(input("enter no:"))

lastevennum = 2 * n

evennum = lastevennum

for i in range(1,n+1):

    evennum = lastevennum

    for j in range(i):

        print(evennum,end = ' ')

        evennum -= 2

    print(' ')

'''
output : 

enter no:5
10
10 8
10 8 6
10 8 6 4

'''