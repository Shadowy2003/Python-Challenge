#This is a program that supplies all the prime numbers between two boundaries - the upper limit and the lower limit - as given by the user

prime_numbers = []
remainder = []

a = input("Lower limit of range: ")
b = input("Upper limit of range: ")

a = a.replace(" ", "") #removes any spaces in the input
a = a.replace(",", '') #removes any commas in the input

b = b.replace(" ", "") #removes any spaces in the input
b = b.replace(",", '') #removes any commas in the input
b = int(b) #comverts the string to integer

div = 1
num = int(a)

while num <= b:
    while div <= b:
        remainder.append(num % div)
        div += 1
    
    if remainder.count(0) == 2:
        prime_numbers.append(num)
    else:
        pass
        
    remainder = []
    div = 1
    num += 1

print(" ")
print(prime_numbers) 