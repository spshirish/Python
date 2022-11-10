'''
Nested if else
=============
When there is need to give decision based on more than
one condition.

syntax:

if Condition1: T | T | F
 
   if Condition2: T | F
   
     execute if block.
   else:
   
      excute else block.
else:
    
	if Condition3:T | F
	  excute if block.
	  
	else:
	  excute else block.

checking
========
step1:first check for zero and non-zero
step2:if zero then display neither positive nor negative.
step3:if non-zero, then further check for positive and negative.
  
'''

print("Enter number:")
n=int(input())#n=15,-7,0

if n==0:#0==0 T,-7==0 F
    print("Number is neither positive nor negative")
else:

    if n>0:#15>0 T,-7>0 F,0>0 F
        print("Positive number")

    else:
        print("Negative Number")


