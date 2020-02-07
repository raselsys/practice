n = int(input('Enter num of Row you want:'))
for row in range (1, n+1):
    for col in range (1, 2*n+1):
        if col not in range(row+1, (2*n+1)-row):
            if col%2==1 and col<=n:
                print('O', end=' ')
            elif col%2==0 and col>n:
                print('O', end=' ')
            else: print('1', end=' ')
        else : print (' ', end= ' ')
    print()
