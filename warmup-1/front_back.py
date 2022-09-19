'''

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''
str = 'kitten'
print(str[::-1])
print(str.replace(str[0],str[5]))
'''def front_back(str):'''