from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0

        for sentence in sentences:
            count = 1

            for ch in sentence:
                if ch == " ":
                    count += 1

            if count > ans:
                ans = count

        return ans