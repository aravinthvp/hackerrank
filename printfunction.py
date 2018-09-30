#Read an integer N.

#Without using any string methods, try to print the following:

#1,2,3....N

#Note that "...." represents the values in between. 


#solution

if __name__ == '__main__':
    n = int(input())
    for a in range(n):
        print(a+1,end="")