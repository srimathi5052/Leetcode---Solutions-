class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        res = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            cur = queue.popleft()

            if isValid(cur):
                res.append(cur)
                found = True

            if found:
                continue

            for i in range(len(cur)):
                if cur[i] not in '()':
                    continue
                nxt = cur[:i] + cur[i+1:]
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return res