class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set1 = set()

        for i in sentence:
            set1.add(i)

        return len(set1) == 26