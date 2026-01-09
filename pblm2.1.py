# An n-digit number is SPECIAL if the addition of its sum of the digits and the product
# of its digits equals to the original number. E.g., 19 is a SPECIAL 2-digit number. Write a
# program to verify whether a given number is SPECIAL or not. Extend this program to verify
# whether there exists any SPECIAL number for a given value of number of digits n.
def is_special_number(num):
    original_num = num
    sum=0
    product=1
    while num>0:
        digit=num%10
        sum+=digit
        product*=digit
        num=num//10
    if sum+product==original_num:
        return True 
    else:
        return False

print(is_special_number(19))   
