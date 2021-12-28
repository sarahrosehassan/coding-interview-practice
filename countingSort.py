# Given a list of integers, count and return the number of times each value appears as an array of integers.
# countArr = [0,0,0,0,0]
# arr[1,1,3,2,1]

def countingSort(arr):
    countArr = [0] * 100
        
    for i in range (len(arr)):
        countArr[arr[i]] += 1
        
    return countArr
