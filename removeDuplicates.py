    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # remove duplicates from sorted array
        # deleting and shifting the elements behind is O(n)
        # Traversing takes O(n)
        # Total Time Complexity: O(n*n)
        
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
