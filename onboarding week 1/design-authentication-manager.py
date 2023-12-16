class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.my_dict = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.my_dict[tokenId] = currentTime + self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.my_dict[tokenId] <= currentTime:
            return
        self.my_dict[tokenId] = currentTime + self.time
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for expirdate in self.my_dict.values():
            if expirdate > currentTime:
                count += 1 
        return count 

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)