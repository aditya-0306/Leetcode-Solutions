class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w
            
        rows, cols = len(board), len(board[0])
        res = set()
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
                
            nxt_node = node.children[char]
            if nxt_node.word:
                res.add(nxt_node.word)
                
            board[r][c] = "#"  # Mark as visited
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt_node)
            board[r][c] = char  # Backtrack
            
            # Optional optimization: prune trie leaf nodes
            if not nxt_node.children:
                del node.children[char]
                
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
                
        return list(res)
        