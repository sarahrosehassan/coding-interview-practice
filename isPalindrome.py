# two line Python solution

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        alNumString = re.sub(r'[^A-Za-z0-9]+', '', s).lower() # remove all occurences of non-alphanumeric characters from raw-string and convert to lower case 

        return alNumString == alNumString[::-1] # check if string with all non-alphanumeric characters removed is the same as reversed string
    
    """
    Explanation of regular expression r'[^A-Za-z0-9]+'
    ^ not
    r raw-string to ignore escape sequences. For example, print(r'\n') prints \n not a new line
    + to match one or more characters
    Time Complexity: O(n) (faster than 96.04 % of Python online submissions)
    Memory Usage: 15.5 MB (less than 22.54 of Python online submissions)
    """
