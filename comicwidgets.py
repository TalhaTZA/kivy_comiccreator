from kivy.uix.relativelayout import  RelativeLayout
from kivy.uix.scatter import Scatter
from kivy.graphics import Line
class DraggableWidget(Scatter):

    def __init__(self, **kwargs):
        self.selected=None
        self.touched= False
        self.ix=0
        self.iy=0
        super().__init__(**kwargs)

    def on_touch_down(self,touch):
        if self.collide_point(touch.x,touch.y):
            self.touched=True
            self.select()
            return super().on_touch_down(touch)
            #return True
        return super().on_touch_down(touch)

    def select(self):
        if not self.selected:
            self.ix =self.center_x
            self.iy =self.center_y
            with self.canvas:
                self.selected = Line(rectangle=(0, 0, self.width, self.height), dash_offset=2)

    def on_pos(self,instance,value):
        if self.selected and self.touched :
            go=self.parent.general_options
            go.translation=(self.center_x-self.ix,self.center_y-self.iy)
            self.ix=self.center_x
            self.iy=self.center_y

    def on_rotation(self,instance,value):
        if self.selected and self.touched:
            go=self.parent.general_options
            go.rotation=value

    def on_scale(self,instance,value):
        if self.selected and self.touched:
            go=self.parent.general_options
            go.scale=value

    '''def on_touch_move(self,touch):
        (x,y)= self.parent.to_parent(touch.x,touch.y)
        if self.selected and self.touched and self.parent.collide_point(x-self.width/2,y-self.width/2):
            go=self.parent.general_options
            go.translation=(touch.x-self.ix,touch.y-self.iy)
            #self.translate(touch.x-self.ix , touch.y-self.iy)
            return True'''

    def translate(self,x,y):
        self.center_x= self.ix = self.ix + x
        self.center_y= self.iy = self.iy + y

    def on_touch_up(self,touch):
        self.touched=False
        if self.selected:
            if not self.parent.general_options.group_mode:
                self.unselect()
                #return True
        return super().on_touch_up(touch)

    def unselect(self):
        if self.selected:
            self.canvas.remove(self.selected)
            self.selected=None

class StickMan(DraggableWidget):
    pass