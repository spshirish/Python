'''
summation of  1 to n 
'''

n=int(input("Enter last term:"))#n=4
s=0
for i in range(1,n+1,1):#(1,5,1)=>[1,2,3,4]

    s=s+i

print("Summation is:",s)

'''
i   i in []   s=s+i    i step 1
1   1 in[]T   s=0+1=1  2
2   2 in[]T   s=1+2=3  3
3   3 in[]T   s=3+3=6  4
4   4 in[]T   s=6+4=10 5
5   5 in[]F
'''
