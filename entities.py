import random

class Fallings:
    def __init__(self, x, y, scalex, scaley) -> None:
        self.x = x
        self.y = y
        self.scalex = scalex
        self.scaley = scaley

        self.collected = 0 
        self.missed = 0
        self.fallArr = []
        self.fallAtOnce = 6
        self.recentlyEscapedTimer = 0
        self.recentlyCollectedTimer = 0 
    
    def update(self, sliderObj):

        if self.recentlyEscapedTimer > 0:
            self.recentlyEscapedTimer -= 1
        
        if self.recentlyCollectedTimer > 0:
            self.recentlyCollectedTimer -= 1


        for _ in range(self.fallAtOnce - len(self.fallArr)):
            self.fallArr.append(FallObj(
                delay = random.randint(0,500),
                size = 64*self.scalex,
                x = random.randint(int(64*self.scalex),int(self.x-(64)*self.scalex)),
                y = -64*self.scaley,
                vy = 4*self.scaley,
                ))

        for obj in self.fallArr:
            obj.update()
            if obj.y > self.y:
                self.fallArr.remove(obj)
                self.missed += 1
                self.recentlyEscapedTimer = 50
        
            if obj.x <= sliderObj.right and obj.x+obj.size >= sliderObj.left and obj.y+obj.size > sliderObj.top and obj.y < sliderObj.bottom:
                self.fallArr.remove(obj)
                self.collected += 1
                self.recentlyCollectedTimer = 50


class FallObj:
    def __init__(self, delay, size, x, y, vy, vx = 0) -> None:
        self.delay = delay
        self.size = size
        self.x = x
        self.y = y
        self.vx =vx
        self.vy=vy
    
    def update(self):
        if self.delay <= 0:
            self.y = self.y + self.vy 
        else:
            self.delay = self.delay - 1