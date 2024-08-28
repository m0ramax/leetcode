# 567. Permutation in String

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.

def checkInclusion(s1: str, s2: str) -> bool:
    len_s1, len_s2 = len(s1), len(s2)

    if len_s1 > len_s2:
        return False
    
    seen_s1 = {}
    for char in s1:
        seen_s1[char] = seen_s1.get(char,0) + 1
    
    window_count = {}
    for i in range(len_s1):
        char = s2[i]
        window_count[char] = window_count.get(char,0)+1

    if seen_s1 == window_count:
        return True

    for i in range(len_s1, len_s2):
        start_char = s2[i - len_s1]
        new_char = s2[i]

        window_count[new_char] = window_count.get(new_char, 0) + 1

        if window_count[start_char] == 1:
            del window_count[start_char]
        else:
            window_count[start_char] -= 1
        
        if seen_s1 == window_count:
            return True
    return False

print(checkInclusion("ab","eidbaooo"))
print(checkInclusion("ab","eidboaoo"))