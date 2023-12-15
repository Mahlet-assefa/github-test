class FrequencyTracker:

    def __init__(self):
        self.freq=defaultdict(int)
        self.dif=defaultdict(int)
    def add(self, number: int) -> None:
        self.number=number
        if self.freq[self.dif[number]]>0:
            self.freq[self.dif[number]] -= 1
        self.dif[number] += 1
        self.freq[self.dif[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.dif[number]==0:
            return
        self.freq[self.dif[number]] -= 1
        self.dif[number] -= 1
        self.freq[self.dif[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency]>0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)