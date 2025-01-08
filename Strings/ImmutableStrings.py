'''

Strings are immutable:Once we declare the string we can not modify if, if we try
to modify the string it will create new string.

2.If new string does not hava any reference variable then it will be 
removed.
'''

#s1='KodNest'
#s1=s1.upper()
#print(s1)


#s1='K'
#print(s1, id(s1))

s1='Hello'
s2='World'
print(s1, id(s1))
print(s2,id(s2))

print('s1 ID of H:',id(s1[0])) 
print('s1 ID of W:',id(s1[0]))

print('s2 ID of o:',id(s2[1]))
print('s2 ID of o:',id(s2[-1]))


print('s1 ID of l:',id(s1[2]))
print('s1 ID of l:',id(s1[3]))
print('s2 ID of l:',id(s2[3]))
