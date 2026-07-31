class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import Counter


        bulls = 0
        s = []
        g = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                s.append(secret[i])
                g.append(guess[i])

        sc = Counter(s)
        gc = Counter(g)

        cows = 0
        for ch in sc:
            cows += min(sc[ch], gc[ch])

        return "{}A{}B".format(bulls, cows)