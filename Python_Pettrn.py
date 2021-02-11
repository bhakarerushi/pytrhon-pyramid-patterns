
# Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers

n = int(input("enter no:"))

for i in range(1,n+1):
    num = 1
    for j in range(n,0,-1):

        if j > i:
            print(" ",end=' ')
        else:
            print(num, end = ' ')

            num += 1
    
    print(' ')



'''


output : 

enter no:5
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5


'''