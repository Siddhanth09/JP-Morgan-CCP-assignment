
#Task 1 - 
#Given an integer, n, perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird



x=int (input("enter the value with in 100 to 1\n"))
if (x<=100 & x>=1):
    print("Not Weird")
else:
    print("Weird")
if x%2==0:
    print("n is even")
else:
        print("n is odd \n weird")

if x>=20:#greter the 
    print("n is greter than 20 is not weird")
else:
        print("less than 20 n is weird")
        
    
