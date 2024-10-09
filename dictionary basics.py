# dictionary basics

stu_info = {
    'name':'Nazmul',
    'batch':47,
    'dept':'CSE',
    'passing year':2027
}

print(stu_info)
# prints all keys and values as a list

print(stu_info['batch'])
# prints the value of key in []

print(stu_info['passing year'])
# prints the value of 'passing year'
print(stu_info['name'],stu_info['dept'])

stu_info['name'] = 'Sami'
# changes the value of 'name' key to Sami

print(stu_info)
# prints the changed value

stu_info.update({'dept':'BBA','passing year':2024})    
# updates the keys values.

print(stu_info)
# prints it

stu_info.update({'gender':'male'})
# appends or  adds a new key with value at the end

print(stu_info)
#prints it

n = stu_info.get('gender')
# gets gender key value and returns it

print(n)
#prints it

p = stu_info.pop('name')
# pops value of key and stores it

print(stu_info,p)
# prints it

q = stu_info.popitem()
# pops last key and its value stores 
# them in a variable as a tuple

print(stu_info,q)
# prints it

del stu_info['batch']
# deletes the key and its value

print(stu_info)
# prints it

print(stu_info.values())
# prints only values

print(stu_info.keys())
# prints only keys

print(stu_info.items())
# prints keys and values as a tuple in list

for i in stu_info:
    print(i)
# sotores each key or dictionary 

for i,j in stu_info.items():
    print(i,'\t: ',j)
# i stores key and j stores values
# prints key and values like a table   