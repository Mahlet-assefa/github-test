class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.curr = 0

    def step(self, num: int) -> None:
        self.curr += num
    def getPos(self) -> List[int]:
        n = self.curr % (2*((self.w-1)+(self.h-1)))
        if n < self.w:
            return [n, 0]
        n -= self.w-1
        if n < self.h:
            return [self.w-1, n]
        n -= self.h-1
        if n < self.w:
            return [(self.w-1)-n, self.h-1]
        n -= self.w-1
        return [0, (self.h-1)-n]
    def getDir(self) -> str:
        n = self.curr % (2*((self.w-1)+(self.h-1)))
        if n < self.w:
            return "South" if n == 0 and self.curr else "East"
        n -= self.w-1
        if n < self.h:
            return "North"
        n -= self.h-1
        if n < self.w:
            return "West"
        n -= self.w-1
        return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()