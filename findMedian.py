# Given a list of numbers with an odd number of elements, find the median
def findMedian(arr):
    arr.sort()
    index = round(len(arr) // 2)
    return arr[index]
