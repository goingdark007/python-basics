# string slicing

a = 'Hello World'

print(a[2:11])#prints index 2 to 11-1=10

print(a[:11])
#prints index 0 by default to 11-1=10

print(a[2:])
#prints index 2 to end by default

a = "watermark"

print(a[-4:])
#prints index -4+1=-3 to end by default 

a = "amazing"

print(a[0:7:2])
#prints index 0 to 7-1=6
# skips steps by one for two 
#and by two for three