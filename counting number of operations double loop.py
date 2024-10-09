"""This is a program to count the number of operations
of a double loop"""
print("\tCounting double loop operations")
for i in range (1,39):
    print("-",end = "")
a = int(input("\nEnter the beginning number of n :"))
b = int(input("Enter the finishing number of n :"))
print("\tn\tnumber of operations")

for n in range (a,b+1):
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            count += 1
    print(f"\t{n}\t{count}")