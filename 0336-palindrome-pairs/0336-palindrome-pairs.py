

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        res = set()
        
        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                left = word[:j]
                right = word[j:]
                
                # If left is palindrome, look for reverse of right in map
                if left == left[::-1]:
                    rev_right = right[::-1]
                    if rev_right in word_map and word_map[rev_right] != i:
                        res.add((word_map[rev_right], i))
                        
                # If right is palindrome, look for reverse of left in map
                if right == right[::-1]:
                    rev_left = left[::-1]
                    if rev_left in word_map and word_map[rev_left] != i:
                        res.add((i, word_map[rev_left]))
                        
        return list(res)
        