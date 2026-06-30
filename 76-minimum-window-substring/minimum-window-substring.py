class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        required = len(need)
        formed = 0
        window = {}

        left = 0
        ans = (float("inf"), 0, 0)

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                ch = s[left]
                window[ch] -= 1

                if ch in need and window[ch] < need[ch]:
                    formed -= 1

                left += 1

        if ans[0] == float("inf"):
            return ""

        return s[ans[1]:ans[2] + 1]