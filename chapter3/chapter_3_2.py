def collatz(number):
    if number%2==0:
        return number//2
    else :
        return 3*number+1

try:
    u = int(input("Enter the dragon "))
    while collatz(u)!=1:
        print (collatz(u))
        u = collatz(u)
    print(1)
except ValueError:
   print("Please enter an integer") 

