n = int(input("Enter decimal number: "))
p = n
s = 0
k = 0
while (n>0):
    r = n%2
    n = n//2
    k = (10*k)+r

## Store 'k' in the variable 'z'
z = k
##print ("The value of ", p, "in base 2 is: ", z )
## REVERT 'k' (or maybe z :D) Use variables r and s.

while (k>0):
    r = k%10
    s = (10*s)+r
    k = k//10

print("The value of ", p, "in base 2 is: ", s )
