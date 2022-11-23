'''
String
======
1)String is a collection of characters.
2)They are enclosed in single quote or double quote or
  triple quoted.
3)String are immutable i.e once string is formed it
  cannot be changed.[No addition,No replace and No delete]

'''

#x='Itvedant'
'''
x=This is a string
multiline string
itvedant eclass learning
string
'''

x="Itvedant-Eclass"


print(x)
print(type(x))

#len(): This is used to calculate number of characters in the string.

n=len(x)
print("Total number of characters:",n)

#indexing
'''
Need: To process string character by character , there is need
to access character in the string. Indexing helps you to access
character in the string.
There are two types of indexing
1)Positive indexing
2)Negative indexing

Positive index                    x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
        
syntax for accessing:
====================
 string_variable[index_number]

'''
'''
print(x[7])
print(x[12])
#print(x[16])#Error=>index out of range
print(x[-11])
print(x[-14])
'''


#slicing
'''
Need of slicing:
==============
If there is need to extract partial part of the string from
entire string , then use slicing.

1) to reverse string.

syntax:

string_variable[start:stop:step]
                                   x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

Extract vedant word from the give string.

start=>2  stop=>8  step=>1
'''

#x1=x[2:8:1]
#x1=x[10:15:1]

#x1=x[2:12:2]#step 2
#x1=x[2:8:]#default step in slicing is 1
#x1=x[:8:]#default start is 0
#x1=x[::]#default stop = string end

#print(x1)

'''
slicing with negative index

                        Negative Index                  
          I   t   v  e   d   a  n   t -  E  c   l  a  s  s 
          0   1   2  3   4   5  6   7 8  9 10  11 12 13 14
        -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

step=> negative

conclusion:
if step is positive then start=left  end=right
if step is negative then start=right end=left
'''

#x1=x[14:8:-1]#14,13,12,11,10,9
#x1=x[:2:-1]
#x1=x[::-1]
#print(x1)

#print("With Index:")
#for loop using index
'''
                                   x

                   I t v e d a n t - E c  l  a  s  s
                   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

'''
'''               #15
for i in range(0,len(x),1):

    print(x[i])


#without index
print("Without Index:")

for i in x:#for i in "I t v e d a n t - E c  l  a  s  s"

    print(i)

'''

print(x[2])
x[2]="O"  #Item assignment
print(x[2])














