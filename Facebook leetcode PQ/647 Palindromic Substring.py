class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
             #for odd length
            result += self.countPali(s, i, i)
             # for even length
            result += self.countPali(s, i, i+1)
        return result
                
    def countPali(self, s, l, r):
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
                    result +=1
                    l -= 1
                    r += 1
        return result