num = int(input("Enter any Number: "))
count = 0
i = 2

while(i <= num//2):  #if divisable by itself
    if(num % i == 0): # if any remainders
        count = count + 1 # Got this equation from tutorialgateway.org
        break
    i = i + 1

if (count == 0 and num != 1): #conditional critera to check the boxes for prime numbers
    print("%d is a Prime Number" %num)
else:
    print("%d is not a Prime Number" %num)
