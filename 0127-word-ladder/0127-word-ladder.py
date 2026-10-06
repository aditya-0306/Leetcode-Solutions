

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        # Pre-process dictionary to find generic wildcard states
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
                
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            curr_word, level = queue.popleft()
            
            if curr_word == endWord:
                return level
                
            for i in range(len(curr_word)):
                intermediate_word = curr_word[:i] + "*" + curr_word[i+1:]
                
                for neighbor in all_combo_dict[intermediate_word]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                
                # Clear out processed connections to avoid re-visiting
                all_combo_dict[intermediate_word] = []
                
        return 0
        