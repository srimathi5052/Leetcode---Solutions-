class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                if (part.startswith("0") and len(part) > 1) or int(part) > 255:
                    continue

                path.append(part)
                backtrack(start + length, path)
                path.pop()

        backtrack(0, [])
        return result