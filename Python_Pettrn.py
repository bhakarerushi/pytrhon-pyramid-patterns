
#  Inverted Equilateral triangle with star (*) symbol.

n = int(input("enter no:"))

m = (2 * n) - 2
for i in range(n,-1,-1):

    for j in range(0,m):

        print(end = ' ')
    
    m = m+1


    for j in range(i,0,-1):
        print('*', end=' ')

    print(' ')



'''

output : 
enter no:10
                  * * * * * * * * * *  
                   * * * * * * * * *
                    * * * * * * * *
                     * * * * * * *
                      * * * * * *
                       * * * * *
                        * * * *
                         * * *
                          * *

'''