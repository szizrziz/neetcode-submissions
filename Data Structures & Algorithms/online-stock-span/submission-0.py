class StockSpanner:

    def __init__(self):
        self.st=[] #pair(price,span)
    def next(self, price: int) -> int:
        span=1
        #self.st because I need to check if my stack is not empty so that im not accessing a value from emty stack or popping from empty stack, t gives index error
        while self.st and self.st[-1][0]<=price:
            span+=self.st[-1][1]
            self.st.pop()
        self.st.append((price,span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)