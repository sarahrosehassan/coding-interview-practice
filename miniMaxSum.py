# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
def miniMaxSum(arr):
    arr.sort()
    minArr = arr[:4]
    maxArr = arr[1:] 
    print(sum(minArr), sum(maxArr))
