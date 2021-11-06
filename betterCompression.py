# The goal is to compress 'a3c9b2c1' to 'a3b2c10'
def betterCompression(s):
    expandedString = '' #expand string to aaacccccccccbbc
    count = ''
    for char in reversed(s):
        if char.isdigit():
            count += char
        else:
            expandedString += char * int(count)
            count = ''

    frequencyDict = {} #count frequency of each letter in expandedString
    for i in expandedString:
        if i in frequencyDict:
            frequencyDict[i] += 1
        else:
            frequencyDict[i] = 1
    frequencyDict = sorted(frequencyDict.items())

    string=''
    for key,val in frequencyDict:
        string += key + str(val)
    print(string)

betterCompression('a3c9b2c1')
