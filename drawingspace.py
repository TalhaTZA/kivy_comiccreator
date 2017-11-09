
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stencilview import StencilView

class DrawingSpace(StencilView):
    def on_children(self,instance,value):
        self.status_bar.counter = len(self.children)