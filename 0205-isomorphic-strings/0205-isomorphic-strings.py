class Solution:
    def isIsomorphic(self, s, t):
        mapping = {}
        used = set()

        for a, b in zip(s, t):
            if a in mapping:
                if mapping[a] != b:
                    return False
            else:
                if b in used:
                    return False

                mapping[a] = b
                used.add(b)

        return True