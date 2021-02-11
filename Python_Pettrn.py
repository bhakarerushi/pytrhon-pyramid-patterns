
# Connected Inverted pyramid pattern of Numbers .

n = int(input("enter no:"))

for i in range(0,n+1):

    for j in range(n,i,-1):
        print(j,end = ' ')

    for I in range(i):
        print('', end = '')
    
    for k in range(i+1,n+1):
        print(k,end= ' ')
    

    print(' ')


'''

enter no:5
5 4 3 2 1 1 2 3 4 5
5 4 3 2 2 3 4 5
5 4 3 3 4 5
5 4 4 5
5 5

'''
