class Solution:
    def isAnagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False


# Examples
print(isAnagram("racecar", "carrace"))  # True
print(isAnagram("jar", "jam"))          # False
