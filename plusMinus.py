# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero
# Print the decimal value of each fraction on a new line with  places after the decimal

def plusMinus(arr):
    positiveNums = 0
    negativeNums = 0
    zeroes = 0
    arrSize = len(arr)
    
    for num in arr: # count num of positive, negtives and zeroes
        if num < 0 :
            negativeNums += 1
        if num > 0:
            positiveNums += 1
        elif num == 0:
            zeroes += 1
     
    print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(positiveNums/arrSize, negativeNums/arrSize, zeroes/arrSize)) # print each float up to 6th decimal place
