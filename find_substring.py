# Returns the index where the first occurence of the substring is located. "*" represents any letter
def firstOccurrence(s,x):
    sindex = 0
    subindex = 0
    while sindex < len(s): # if letter in s and sub don't match
        if s[sindex+subindex] != x[subindex] and x[subindex] != "*":
            sindex += 1
            subindex = 0

        # if letter in s and sub do match
        if (s[sindex+ subindex]) == x[subindex] or x[subindex == "*"]:
            subindex += 1

        # if all letters in sub match
        if subindex == len(x):
            return sindex
    return -1

firstOccurrence("xabcdey", "ab*de")
