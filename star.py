n = int(input())

k = n*2 -1

for i in range (1, n+1):
    print ((n-i)*' ' + (2*i-1)*'*', end=' ')
    # print(i)
    print ()
    k = k-2
