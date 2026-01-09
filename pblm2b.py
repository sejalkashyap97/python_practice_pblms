#get special numbers in a given range
from pblm2a import is_special_number
def get_special_num_one_way(n):
    for i in range(1,n+1):
        if is_special_number(i) is True:
            print(i,end=" ")
def get_special_num_second_way(n):
    for i in range(1,n+1):
        sum=0
        product=1
        num=i
        while num>0:
            digit=num%10
            sum+=digit
            product*=digit
            num=num//10 
        if sum+product==i:
            print(i,end=" ")  
get_special_num_second_way(200)