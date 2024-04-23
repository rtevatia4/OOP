"""
a legacy Rectangle component's display() method expects to receive "x, y, w, h" parameters. 
But the client wants to pass "upper left x and y" and "lower right x and y". 
This incongruity can be reconciled by adding an additional level of indirection – i.e. an Adapter object.
"""
class LegacyRectangle:
    def display(self, x,y,w,h):
        print(f"Recatangle: x={x}, y={y}, w={w}, h={h}")
    
#adapter class
class RectangleAdapter:
    def __init__(self, legacy_rec: LegacyRectangle):
        self.legacy_rec = legacy_rec
    
    def display(self, x1,y1,x2,y2):
        width = x2-x1
        height = y2-y1
        self.legacy_rec.display(x1,y1,width,height)

#client
legacy_rectangle = LegacyRectangle()
adapter = RectangleAdapter(legacy_rectangle)

# Client wants to pass "upper left x and y" and "lower right x and y"
upper_left_x = 10
upper_left_y = 20
lower_right_x = 30
lower_right_y = 40

# Call the adapted display method using the adapter
adapter.display(upper_left_x, upper_left_y, lower_right_x, lower_right_y)