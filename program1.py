class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
         stack = []

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if len(stack) < 1:
                    return False
                if not self.check(stack, ch):
                    return False

        return len(stack) == 0
        pass







    



  

