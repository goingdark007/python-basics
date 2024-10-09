a = int(input("Enter the number"))

b = 2 

if a <= 1:
    print('not prime')
else:
    c = 0
    while b <= 10:#or can use a//2
        if a != b and a % b == 0:
            c += 1
            break
        b += 1            

    if c == 0:
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")   
    