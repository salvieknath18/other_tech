# https://leetcode.com/problems/word-search-ii/

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_ending_word = False


class Trie:

    def __init__(self):
        self.root = TreeNode("")

    def add_word(self, word):
        node = self.root
        if word:
            for w in word:
                if w in node.children:
                    node = node.children[w]
                else:
                    node.children[w] = TreeNode(w)
                    node = node.children[w]

            node.is_ending_word = True

    def print(self):
        node = self.root
        q = deque()
        q.append(self.root)

        while q:
            node = q.pop()
            print(node.val + "" + str(node.is_ending_word))
            for k, v in node.children.items():
                q.append(v)


def dfs(board, i, j, node, result, visited, m, n, current_str):
    if i < 0 or i >= m or j < 0 or j >= n or visited[(n * i) + j]:
        return

    char = board[i][j]

    if char in node.children:
        ch_node = node.children[char]
        new_str = current_str + char
        if ch_node.is_ending_word:
            result.add(new_str)

        visited[(n * i) + j] = True

        # bottom
        dfs(board, i + 1, j, ch_node, result, visited, m, n, new_str)
        # top
        dfs(board, i - 1, j, ch_node, result, visited, m, n, new_str)
        # right
        dfs(board, i, j + 1, ch_node, result, visited, m, n, new_str)
        # left
        dfs(board, i, j - 1, ch_node, result, visited, m, n, new_str)

        visited[(n * i) + j] = False


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for w in words:
            trie.add_word(w)

        m = len(board)
        n = len(board[0])
        result = set()
        visited = [False] * (m * n)

        for i in range(m):
            for j in range(n):
                dfs(board, i, j, trie.root, result, visited, m, n, "")

        return list(result)


s = Solution()
print(s.findWords([["a","a"]],["a"]))
