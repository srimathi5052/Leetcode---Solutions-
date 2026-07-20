class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        class TrieNode:
           def __init__(self):
             self.children = {}
             self.word = None



        root = TrieNode()

        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == '#'
            ):
                return

            ch = board[r][c]
            if ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word:
                result.append(next_node.word)
                next_node.word = None   # Avoid duplicates

            board[r][c] = '#'

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = ch

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return result