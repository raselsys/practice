n = int(input('Enter a value:'))

num= 1
for r in range (1, n*2, 2):
    for c in range (1, r+1, 2):
        print (num, end=' ')
        num +=2
    print()
