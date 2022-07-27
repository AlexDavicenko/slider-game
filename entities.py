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
        self.timeF = 1

    def update(self, sliderObj):
        
        if self.recentlyEscapedTimer > 0:
            self.recentlyEscapedTimer -= 1*self.timeF
        
        if self.recentlyCollectedTimer > 0:
            self.recentlyCollectedTimer -= 1*self.timeF


        for _ in range(self.fallAtOnce - len(self.fallArr)):


            xpos = random.randint(int(64*self.scalex),int(self.x-(2*64)*self.scalex))
            for obj in self.fallArr:
                pass

            self.fallArr.append(FallObj(
                timeF = self.timeF,
                delay = random.randint(0,500),
                size = 64*self.scalex,
                x = xpos,
                y = -64*self.scaley,
                vy = 4*self.scaley,
                ))

        for obj in self.fallArr:
            obj.timeF = self.timeF
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
    def __init__(self, timeF, delay, size, x, y, vy, vx = 0) -> None:
        self.delay = delay
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy 
        
        self.timeF = timeF


    def update(self):
        if self.delay <= 0:
            self.y = self.y + self.vy *self.timeF
        else:
            self.delay = self.delay - 1*self.timeF