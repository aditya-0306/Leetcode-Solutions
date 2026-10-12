

class FreqStack:
    def __init__(self):
        self.freq = Counter()
        self.freq_to_stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        if f > self.max_freq:
            self.max_freq = f
        self.freq_to_stack[f].append(val)

    def pop(self) -> int:
        val = self.freq_to_stack[self.max_freq].pop()
        self.freq[val] -= 1
        
        if not self.freq_to_stack[self.max_freq]:
            self.max_freq -= 1
            
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()