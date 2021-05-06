matriz = [[1,2,3,4,5,6],
          [7,8,9,10,11,12],
          [0,0,1,16,17,18],
          [0,1,0,7,23,24],
          [1,7,6,5,4,3]]

kernel = [[1,1,1],[0,0,0],[2,10,3]]

for row in matriz:
        for col in row:
            print(col ,end=' ')
        print(end='\n')

print('\n')

for row in kernel:
        for col in row:
            print(col ,end=' ')
        print(end='\n')