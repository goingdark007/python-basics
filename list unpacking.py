def sum(a,b,c):

    return a+b+c

list = [2,3,5]

print(sum(*list))
# * before the list unpacks the list elements in serial order
# gives the value in functions