

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
            
        # Distance map from beginWord to each word
        distance = {beginWord: 0}
        # Graph mapping child -> list of parents on shortest paths
        parents = defaultdict(list)
        
        queue = deque([beginWord])
        found = False
        
        while queue and not found:
            visited_this_level = set()
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                curr_dist = distance[curr]
                
                if curr == endWord:
                    found = True
                    continue
                    
                # Generate all generic neighbor states
                for i in range(len(curr)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = curr[:i] + c + curr[i+1:]
                        if next_word in word_set:
                            if next_word not in distance:
                                distance[next_word] = curr_dist + 1
                                queue.append(next_word)
                                visited_this_level.add(next_word)
                            
                            if distance[next_word] == curr_dist + 1:
                                parents[next_word].append(curr)
                                
            word_set -= visited_this_level
            
        res = []
        if not found:
            return res
            
        def dfs(word, path):
            if word == beginWord:
                res.append([beginWord] + path[::-1])
                return
            for p in parents[word]:
                path.append(word)
                dfs(p, path)
                path.pop()
                
        dfs(endWord, [])
        return res
        