#Error handling

#try:
    #some risky code
#except some exception:
    #handles error 
#finally:
    #runs the code error or no error

n = 0

try:
    n = int(input('type :'))
    # input has to be int or error
  
except ValueError:
    print('Invalid input entr a number')  
    #ValueError handles the error and prints
    
finally:
    print(n)   
    # finally runs the code no matter what 
    
while True:
    # error handling in loop
    try:
        n = int(input('enter :'))  
        #checks for error
    except ValueError:
        print('Invalid input') 
        #if error is found prints it
        
        continue
        # skips this iterations starts the loop again
        
    finally:
        # not necessary to write finally in this loop
        print(n)
        #prints it 
          
        break    
        # breaks and stops the loop