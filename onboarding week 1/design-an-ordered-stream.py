class OrderedStream:

    def __init__(self, n: int):
        self.i=0
        self.values = [None]*n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.values[idKey]=value
        result=[]
        if self.i != idKey:
            return result
        while self.i<len(self.values) and self.values[self.i]:
            result.append(self.values[self.i])
            self.i += 1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)