'''
Greatest of the three number entered by user.
'''

a=int(input("Enter first Number:"))#70,70
b=int(input("Enter Second Number:"))#50,50
c=int(input("Enter Third Number:"))#20,100

if a>b:#70>50 T,70>50 T

    if a>c:#70>20 T,70>100 F

        print(a," is greater")

    else:
        print(c,"is greater")

else:

    if b>c:
        print(b,"is greater")

    else:
        print(c,"is greater")
    
