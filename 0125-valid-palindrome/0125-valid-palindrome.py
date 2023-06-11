class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = re.sub(r"[\W_]+|[\s]","",s)
        return new == new[::-1]