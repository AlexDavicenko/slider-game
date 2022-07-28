import random
from pygame import rect

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
                rObj = rect.Rect(
                    xpos,
                    -64*self.scaley, 
                    64*self.scalex, 
                    64*self.scaley),
                timeF = self.timeF,
                delay = random.randint(0,500),
                vy = 4*self.scaley,
            ))

        for i, obj in enumerate(self.fallArr):
            obj.timeF = self.timeF

            obj.update()

            if obj.rObj.top > self.y:
                self.fallArr.remove(obj)
                self.missed += 1
                self.recentlyEscapedTimer = 50
        
            if obj.rObj.colliderect(sliderObj):
                self.fallArr.pop(i)
                self.collected += 1
                self.recentlyCollectedTimer = 50


class FallObj:
    def __init__(self, rObj, timeF, delay, vy, vx = 0) -> None:
        self.delay = delay
        self.rObj = rObj
        self.vx = vx
        self.vy = vy

        self.y = rObj.bottom
        
        self.timeF = timeF


    def update(self):
        if self.delay <= 0:
            self.y += self.vy *self.timeF
            self.rObj.bottom = self.y
        else:
            self.delay = self.delay - 1*self.timeF