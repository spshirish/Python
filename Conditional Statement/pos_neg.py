'''
A number is entered by user , check whether number is positive
or negative number or not.


                        ------------------------
                       -3  -2  -1  0  1  2   3
                         negative< 0 > positive
positive: number must be greater than zero
negative: number must be less than zero
'''

print("Enter number:")
n=int(input())#n=15,-7,0

if n>0:#15>0 T,-7>0 F,0>0 F
    print("Positive number")

else:
    print("Negative Number")

