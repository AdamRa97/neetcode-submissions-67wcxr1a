class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()
        directions = [[0,1], [0,-1],[1,0],[-1,0]]
        res = []
        ROWS, COLS = len(board), len(board[0])
        trie = PrefixTrie()
        for word in words:
            trie.insertWord(word)
        
        def dfs(r,c,node):
            if (r,c) in visited:
                return False
            
            char = board[r][c]
            if char not in node.children:
                return False

            child = node.children[char]
            if child.word:
                res.append(child.word)
                child.word = None
            
            visited.add((r,c))
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row,col) in visited:
                    continue
                dfs(row,col, child)
            visited.remove((r,c))
            if not child.children and not child.word:
                del child

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie.root)
        return res