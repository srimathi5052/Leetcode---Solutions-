class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter


        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)

        result = []

        for i in range(word_len):
            left = i
            count = 0
            seen = {}

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_freq:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    seen.clear()
                    count = 0
                    left = right + word_len

        return result