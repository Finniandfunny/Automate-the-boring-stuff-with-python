#The first two chapters don't have such project
# This project is mainly to learn about python functions 

# declare a function with the given instruction 
def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else :
        print(3*number+1)
        return 3*number+1

#call the function
u = int(input("Enter the dragon"))
while u!=1:
    u = collatz(u)
