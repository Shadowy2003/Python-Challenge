number = input("Enter number: ") #asks for user input

factors = [] #empty list to store factors
try:
    x = int(number)
    if isinstance(x, int) == True and x > 0: #checks if the number is a positive integer
                    for i in range(1, x+1):
                        if x%i == 0: #tests if a number is a factor of the user inputted number
                            factors.append(i) #stores the number in the list of factors if the test is passed
                        else:
                            pass
    else:
        print("Wrong input!")                            
except ValueError:
    print("Wrong input!")
    
output = ", ".join(str(e) for e in factors[:-1])
print(f"The factors of {number} are: {output} and {factors[-1]}")