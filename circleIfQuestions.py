def circles(radius, color):
    Circle(100, 100, 50, fill='grey')
    if radius < 100:
        Circle(300, 100, radius, fill='blueViolet')
    if color == 'orange':
        Circle(100, 300, 75, fill=color)
    else:
        Circle(300, 300, radius, fill='hotPink')

circles(25, 'Red')

# How many circles are drawn?
# Will a red circle be drawn?
# What is the minimum number of circles that can be drawn?
# What is the maximum number of circles that can be drawn?
