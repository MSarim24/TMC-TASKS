def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

def is_palindrome(x):
    if x<0:
        return False
    s = str(x)
    return s == s[::-1]

print(is_palindrome(121))

print(is_palindrome(-121))



    
def romanToInt(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    for char in s:
        value = roman_numerals[char]
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))

def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))

def validparentheses(str):
    stack  = []
    for char in str:
        if char in '({[':
            stack.append(char)

        if char == ')':
            if stack.pop() != '(':
                return False
            
        if char == '}':
            if stack.pop() != '{':
                return False
            
        if char == ']':
            if stack.pop() != '[':
                return False
        
    return len(stack) == 0

print(validparentheses("([[{()}]])"))
print(validparentheses("([)]"))

