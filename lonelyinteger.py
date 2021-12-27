# Given an array of integers, where all elements but one occur twice, find the unique element.
def lonelyinteger(a):
    arrayNoDuplicates = set(a)
    return 2 * sum(arrayNoDuplicates) - sum(a)
