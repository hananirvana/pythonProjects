"""
Find Cost of Tile to Cover W x H Floor -
Calculate the total cost of tile it would
take to cover a floor plan of width and height,
using a cost entered by the user.
"""

def cost(w,h,c):
    return c*(w*h)

cos = int(input("What is the cost of each tile? "))
print('total cost is ${}'.format(cost(cos, 17, 68)))
