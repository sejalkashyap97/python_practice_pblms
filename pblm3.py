#  The abundancy of a natural number n is defined as the rational number σ(n)/n, the
# ratio between the sum of divisors of the number and the number itself. A number n is defined
# as friendly if it shares abundancy with one or more other numbers. This means there might
# exist a pair of numbers i and j such that i ̸ = j but σ(i)/i = σ(j)/ j 
#  For example, 6 and 28 are
# friendly with each other because σ(6)/ 6  =σ(28)/ 28  =2. Write a program to verify whether a pair
# of integers given as user input are friendly or not.
def sum_of_divisors(n):
    sum_div=0
    for i in range(1,n):
        if n%i==0:
            sum_div+=i
    return sum_div
def are_friendly_numbers(i,j):
    abundancy_i=sum_of_divisors(i)/i
    abundancy_j=sum_of_divisors(j)/j
    if abundancy_i==abundancy_j:
        return True
    else:
        return False