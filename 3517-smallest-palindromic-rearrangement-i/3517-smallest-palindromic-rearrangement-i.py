class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        half=n//2
        first="".join(sorted(s[:half]))
        mid=s[half] if n%2 !=0 else ""
        return first+mid+first[::-1]