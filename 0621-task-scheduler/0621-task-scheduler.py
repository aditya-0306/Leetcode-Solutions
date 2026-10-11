

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        # Count how many tasks share this maximum frequency
        max_count = sum(1 for freq in counts.values() if freq == max_freq)
        
        # Formula-based calculation
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
        