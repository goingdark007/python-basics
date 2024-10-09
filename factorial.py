# factorial
n = int(input("Enter the number"))
c = 1
while n >= 1:
    c *= n
    n -= 1
print(f'The sum is {c}')    