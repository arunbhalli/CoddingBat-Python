'''

Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

'''
str = 'kitten'
print(str[::-1])
print(str.replace(str[0],str[5]))

'''print(str[::-1])
for n in range(0,len(str)-1):
 front = str[:n]
 back = str[n+1:]
print(front+back)
'''
    
'''

print(str)
print(str[0])
print(str[0:n:2])
print(str.replace(str[0],''))

'''


  