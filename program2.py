class Solution(object):
     def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  
            return 0
        
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        m = len(s)
        last = roman_map[s[m-1]]
        ans = 0

        for i in range(m-1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                ans -= roman_map[s[i]]
            else:
                ans += roman_map[s[i]]

        ans += last
        return ans


