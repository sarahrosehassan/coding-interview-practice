# first half of elements in the sequence are in increasing order and the last half of elements are in decreasing order
# sort the array - first half will be increasing
# then swap the elements of the second half of the array to get the second half to decrease

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2 - 1) # change 1 - to swap the element exactly in the middle instead of to the right of the middle
    a[mid], a[n-1] = a[n-1], a[mid] # swap the middle element and the last element

    st = mid + 1
    ed = n - 2 # change 2 - already changed the final element, do not need to start there
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # change 3 - go from right to left

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
