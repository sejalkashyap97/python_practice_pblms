#  Two elements A[i] and A[j] of a list A are said to form an inversion pair if
# A[i] > A[j] but i < j. Write a program to count the number of inversion pairs in a list A
# containing distinct integers.
# Note that, for the array A = {8,4,2,1}, the inversion pairs are (8, 4), (4, 2), (8, 2), (8, 1), (4,
# 1) and (2, 1)
def count_inversion_pairs(arr):
    count=0
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                count+=1    
    return count