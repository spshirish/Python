'''

Greatest of three number using logical Operator
'''

a=int(input("Enter first Number:"))#70,70
b=int(input("Enter Second Number:"))#50,50
c=int(input("Enter Third Number:"))#20,100

if a>b and a>c:#70>50 and 70>20 => T and T=>T
    print(a,"is greater")

if b>a and b>c:#50>70 and 50>20 => F and T =>F
    print(b,"is greater")

if c>a and c>b:#20>70 and 20>50 =>F and F => F
    print(c,"is greater")


'''
In user input of a=70,b=50,c=20
First if condition is evaluated to be True and we
got the result of greatest of three numbers.

If we got the result in first if condition, then
ideally there is no need to check further if conditions.
Since in above program its checking other two condition,
there is waster of interpreter time in code execution
which is not  going to give us output.



'''

    
