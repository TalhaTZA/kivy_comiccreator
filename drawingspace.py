
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stencilview import StencilView
from kivy.gesture import Gesture , GestureDatabase
from gestures import line45_str , cirlce_str , cross_str

class DrawingSpace(StencilView):
    
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.gdb=GestureDatabase()
        self.line45=self.gdb.str_to_gesture(line45_str)
        self.cirlce=self.gdb.str_to_gesture(cirlce_str)
        self.cross=self.gdb.str_to_gesture(cross_str)
        self.line135=self.line45.rotate(90)
        self.line225=self.line45.rotate(180)
        self.line315=self.line45.rotate(270)
        self.gdb.add_gesture(self.line45)
        self.gdb.add_gesture(self.line135)
        self.gdb.add_gesture(self.line225)
        self.gdb.add_gesture(self.line315)
        self.gdb.add_gesture(self.cross)
        self.gdb.add_gesture(self.cirlce)
    
    def activate(self):
        self.tool_box.disabled = True
        self.bind(on_touch_down=self.down , on_touch_move=self.move, on_touch_up=self.up)

    def deactivate(self):
        self.unbind(on_touch_down=self.down , on_touch_move=self.move, on_touch_up=self.up)
        self.tool_box.disabled= False

    def down(self,ds,touch):
        if self.collide_point(*touch.pos):
            self.points=[touch.pos]
            self.ix=self.fx=touch.x
            self.iy=self.fy=touch.y
        return True

    def move(self,ds,touch):
        if self.collide_point(*touch.pos):
            self.points+=[touch.pos]
            self.min_and_max(touch.x,touch.y)
        return True

    def up(self,ds,touch):
        if self.collide_point(*touch.pos):
            self.points+=[touch.pos]
            self.min_and_max(touch.x,touch.y)
            gesture=self.gesturize()
            recognized=self.gdb.find(gesture,minscore=0.50)
            if recognized:
                self.discriminate(recognized)
        return True

    def gesturize(self):
        gesture=Gesture()
        gesture.add_stroke(self.points)
        gesture.normalize()
        return gesture
    
    def min_and_max(self,x,y):
        self.ix=min(self.ix,x)
        self.iy=min(self.iy,y)
        self.fx=max(self.fx,x)
        self.fy=max(self.fy,y)

    def discriminate(self,recognized):
        gest=recognized[1]
        if gest== self.cross:
            self.add_stickman()
        if gest==self.cirlce:
            self.add_circle()
        if gest==self.line45:
            self.add_line(self.ix,self.iy,self.fx,self.fy)
        if gest==self.line135:
            self.add_line(self.ix,self.fy,self.fx,self.iy)
        if gest==self.line225:
            self.add_line(self.fx,self.fy,self.ix,self.iy)
        if gest==self.line315:
            self.add_line(self.fx,self.iy,self.ix,self.fy)

    def add_circle(self):
        cx=(self.ix+self.fx)/2.0
        cy=(self.iy+self.fy)/2.0
        self.tool_box.tool_circle.widgetsize(self,cx,cy,self.ix,self.iy)
    
    def add_stickman(self):
        cx=(self.ix+self.fx)/2.0
        cy=(self.iy+self.fy)/2.0
        self.tool_box.tool_stickman.draw(self,cx,cy)
    
    def add_line(self,ix,iy,fx,fy):
        self.tool_box.tool_line.widgetsize(self,ix,iy,fx,fy)

    def on_children(self,instance,value):
        self.status_bar.counter = len(self.children)