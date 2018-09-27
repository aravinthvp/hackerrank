Task
Given an integer, , perform the following conditional actions:

    If is odd, print Weird
    If is even and in the inclusive range of  2 to 5, print Not Weird
    If is even and in the inclusive range of 6 to 20 , print Weird
    If is even and greater than 20 , print Not Weird

	
	
	
Solution
   
   
 #!/bin/python3
 
N=int(input())
if N%2==1:                                                   # If is odd, print Weird
    print("Weird")
else:
    if N>=2 and N<=5:                                     # range of  2 to 5
        print ("Not Weird")
    elif N>=6 and N<= 20:                                # range of 6 to 20
        print ("Weird")
    elif N>20:                                                   # greater than 20 , print Not Weird                                              
        print("Not Weird")
