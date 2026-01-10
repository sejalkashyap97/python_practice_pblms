# Write a program to check whether a number given as user input is a power of 21 or
# not. Accordingly, print POWER OF 21 or NOT POWER OF 21
def is_power_of_21(n):
    if n<=0:
        return False
    while n%21==0:
        n=n//21
    if n==1:
        print
    else:
        print("NOT POWER OF 21")

