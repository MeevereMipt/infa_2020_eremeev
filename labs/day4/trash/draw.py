from labs.day4.trash.event import Eventer

from labs.day4.trash.sprite import *





class ColorGUI():

    def __init__(self, scale=(1,1)):
        self.guiSize = ((100+30)*scale[0],(100)*scale[1])
        self.scale = scale

        self.value = 100

    def renderPalette(self, point) -> Sprite:
        self.point = point
        surface = pg.Surface(self.guiSize)
        for i in range(0,360):
            for j in range(0,100):
                color = pg.Color("#000000")
                color.hsva = (i, j, self.value, 50)
                rect = pg.Rect(i*100/360 * self.scale[0], j*self.scale[1], self.scale[0], self.scale[1])
                pg.draw.rect(surface, color, rect)
        for i in range(0,100):
            color = pg.Color("#000000")
            color.hsva = (0, 0, i, 50)
            rect = pg.Rect(100 * self.scale[0], i * self.scale[1], 30*self.scale[0], self.scale[1])
            pg.draw.rect(surface, color, rect)

        return Sprite(surface,point)

    def getColor(self, pt):
        pos = ( pt[0]-self.point[0] , pt[1]-self.point[1])
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < 100*self.scale[0] and pos[1] < self.guiSize[1]:
            rawcolor = (pos[0] / self.scale[0] / 100 * 360, pos[1] / self.scale[1])
            color = pg.Color("#000000")
            color.hsva = rawcolor[0], rawcolor[1], self.value, 50
            return color
        elif pos[0] >= 100*self.scale[0] and pos[1] >= 0 and pos[0] < 130*self.scale[0] and pos[1] < self.guiSize[1]:
            self.value = pos[1] / self.scale[1]
        return None







class View():

    def __init__(self, display):

        # List of Sprites(?)
        self.renderDict = {}
        self.renderStack = []
        self.display = display


    def pushRender(self, s : Sprite, key=None ):
        if key != None:
            self.renderDict[key] = s
        else:
            self.renderStack.append(s)

    def getRender(self, key):
        if key in self.renderDict:
            return self.renderDict[key]
        else:
            return None

    def removeRender(self, key):
        if key in self.renderDict:
            del self.renderDict[key]

    def onRender(self):
        for sprite in self.renderStack:
            self.display.blit(sprite.surface, sprite.pos, sprite.area)

        for key in self.renderDict:
            sprite = self.renderDict[key]
            self.display.blit(sprite.surface, sprite.pos, sprite.area)




class App(Eventer):


    def __init__(self):
        Eventer.__init__(self)

        pg.init()

        self.FPS = 30
        self.screen = pg.display.set_mode((800, 800))
        self.clock = pg.time.Clock()

        self.view = View(self.screen)

        self.currentColor = [255,255,255]
        self.currentShape = "rect"

        self.colorGui = ColorGUI((2,2))

    def execute(self):
        self.finished = False
        while not self.finished:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
        self.onEnd()

    def onMouseDown(self, event):
        Eventer.onMouseDown(self,event)
        # When left button is pushed, close the color palette if it's open and choose the color
        if event.button == pg.BUTTON_LEFT:
            if self.view.getRender("colorGui") != None:
                color = self.colorGui.getColor(pg.mouse.get_pos())
                if color != None:
                    self.currentColor = color
                self.view.removeRender("colorGui")

        # When right button is pushed, show the color palette
        if event.button == pg.BUTTON_RIGHT:
            if self.view.getRender("colorGui") == None:
                self.view.pushRender(self.colorGui.renderPalette(event.pos), "colorGui")
            else:
                color = self.colorGui.getColor(pg.mouse.get_pos())
                if color != None:
                    self.currentColor = color
                self.view.removeRender("colorGui")

        # When the mouse wheel is pushed, last figure is saved
        if event.button == pg.BUTTON_MIDDLE:
            print("Rect saved")
            rect = self.view.getRender("figure")
            self.view.pushRender(rect)


    def onMouseMotion(self, event):
        if pg.MOUSEBUTTONDOWN in self.currentEvents:
            ev = self.currentEvents[pg.MOUSEBUTTONDOWN]

            self.view.removeRender("figure")
            sprite = None
            if self.currentShape == "rect":
                sprite = spriteRectangle(event.pos, ev.pos, self.currentColor)

            if sprite != None:
                self.view.pushRender(sprite,"figure")


    def onLoop(self):
        pass

    def onRender(self):
        self.screen.fill((0,0,0))
        self.view.onRender()
        pg.display.update()


    def onEnd(self):
        pg.quit()



if __name__ == "__main__":
    app = App()

    app.execute()
