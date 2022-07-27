
import math
import pygame
import sys



from labels import Label
from entities import Fallings
from setup import *


class Game():

    def __init__(self) -> None:
        

        pygame.init()

        info = pygame.display.Info()
        self.x = info.current_w
        self.y = info.current_h
        self.x = 1280
        self.y = 720
        self.scalex = self.x/1920
        self.scaley = self.y/1080


        self.window = pygame.display.set_mode((self.x,self.y))  #pygame.FULLSCREEN|pygame.SCALED
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Slider Game")
        

        #pygame.mixer.music.load("assets/curry.mp3")
        #pygame.mixer.music.play()
        #pineapple = pygame.image.load("assets/pineapple.png")
        #pineapple = pygame.transform.scale(pineapple,[int(64*scalex), int(64*scaley)])

        self.slider = pygame.Rect(
                ((1920/2)-100)*self.scalex,
                (980)*self.scaley,
                200*self.scalex,
                50*self.scaley
                )
        self.fObj = Fallings(self.x,self.y,self.scalex,self.scaley)
        
        
        self.paused = False
        self.tp_set_up = False
        self.tp = None

    def eventloop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused

                if event.key == pygame.K_e and not self.paused:
                    if not self.tp_set_up:
                        self.tp = pygame.Rect(self.slider.left, self.slider.top, self.slider.width, self.slider.height)
                    else:
                        self.slider = pygame.Rect(self.tp.left, self.tp.top, self.tp.width, self.tp.height)



                    self.tp_set_up = not self.tp_set_up

    def drawLabels(self):

        collectedColor = WHITE
        if self.fObj.recentlyCollectedTimer > 0:
            collectedColor = GREEN
        missedColor = WHITE
        if self.fObj.recentlyEscapedTimer > 0:
            missedColor = RED

        Label(
            window = self.window,
            size = 24,
            text = f"{str(self.clock.get_fps())[:4]}",
            color = WHITE,
            x = 10*self.scalex,
            y = 10*self.scaley)

        Label(
        window = self.window,
        size = 24,
        text = f"Collected: {self.fObj.collected}",
        color = collectedColor,
        x = (self.x-(520)*self.scalex),
        y = 10*self.scaley)

        Label(
        window = self.window,
        size = 24,
        text = f"Missed: {self.fObj.missed}",
        color = missedColor,
        x = (self.x-(250)*self.scalex),
        y = 10*self.scaley)


    def mainloop(self):
        while True:
            self.clock.tick(60)

            self.eventloop()




            if not self.paused:
                self.fObj.update(self.slider)  

            keys = pygame.key.get_pressed()

            if not self.paused:
                if keys[pygame.K_a]:
                    if self.slider.left > 0:
                        self.slider.x -= 16 * self.scalex
                if keys[pygame.K_d]:
                    if self.slider.right < self.x:
                        self.slider.x += 16 * self.scalex 

            

            self.window.fill((0,0,0))

            for obj in self.fObj.fallArr:
                
                dispersionFactor = 25*math.sin(obj.y/50)

                pygame.draw.rect(self.window, MAGENTA, pygame.Rect(obj.x + dispersionFactor, obj.y, 64*self.scalex,64*self.scaley))
                #window.blit(pineapple,(obj.x + 25*math.sin(obj.y/50),obj.y))

            if self.tp_set_up:
                pygame.draw.rect(self.window,DARKYELLOW, self.tp)
            pygame.draw.rect(self.window, YELLOW, self.slider)
            
           

            self.drawLabels()
            pygame.display.update()





def main():

    Game().mainloop()

    
if __name__ == "__main__":
    main()


    
