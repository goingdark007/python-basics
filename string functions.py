# string functions

a = "my name is sami"

print(a.capitalize())
# capitalizes the first word in sentence

print(a.upper())
# makes all letters capital case

a = 'Hello World'

print(a.lower())
# makes all letters lowe case

a = 'my name is nazmul'

print(a.title())
# makes the first letter capital
# of every word

a = 'hello'

print(len(a))
# prints number of elements or range

print(a.endswith('lo'))
# matches with the ending letters and 
# displays true or false

print(a.count('l'))
# how many times a letter is repeating

a = 'watermark'

print(a.find('a'))
# finds the index of letter in find('')

a = 'harry'

a = a.replace('r','l')

print(a)
# replaces r with l

a = 'welcome to the jungle'

a = a.split()

print(a)
# splits the string at space by default

a = 'welcome*to*the*jungle'

a = a.split('*')

print(a)
# splits the string at '*'

a = ['welcome', 'to', 'the', 'jungle']

tuple = ('welcome', 'to', 'the', 'tuple')

a = ' '.join(a)

tuple = ' '.join(tuple)

print(a,'\t',tuple)
# merges the list or tuple or split words
# into one and ' ' is added at the joints