'''
for loop
========

syntax:
     for variable in range(start,stop,step):

              body of loop to be repeated


variable is a counter variable.

'''

'''
i=11
r=i in range(1,10,1)#3,11 in [1,2,3,4,5,6,7,8,9]
print(r)
'''

n=int(input("Enter last term:"))#n=15

for i in range(1,n+1,1):#[1,2,3,4,5,6,7,8,9]

        print(i)

'''
i   i in [1,2,...,9]    print(i)    step 1
1   1 in [1,2,...,9]T    1           2
2   2 in            T    2           3
3   3 in []         T    3           4
.
.
.
.
9   9 in []         T    9           10
10 10 in []         F
'''




