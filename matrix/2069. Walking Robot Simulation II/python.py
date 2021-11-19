class Robot:
    
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.d = 0
        self.dir = ['East','North','West','South']
        self.x,self.y = 0,0
        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]
        

    def move(self, num: int) -> None:
        _max = 2*self.w + 2* self.h - 4
        num %= _max
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.d = 3
            if self.x == self.w -1 and self.y ==0:
                self.d = 0
            if self.x == self.w -1 and self.y == self.h - 1:
                self.d = 1
            if self.x == 0 and self.y == self.h - 1:
                self.d = 2
        #steps are [num,1] included
        for i in range(num,0,-1):
            nx = self.dx[self.d] + self.x
            ny = self.dy[self.d] + self.y
            if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
                self.d +=1
                self.d %=4
                nx = self.dx[self.d] + self.x
                ny = self.dy[self.d] + self.y
            self.x = nx
            self.y = ny

    def getPos(self) -> List[int]:
        return [self.x,self.y]        

    def getDir(self) -> str:
        return self.dir[self.d]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()