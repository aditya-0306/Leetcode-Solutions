class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            ok = True

            for ch in word:
                if ch not in allowed:
                    ok = False
                    break

            if ok:
                count += 1

        return count
        