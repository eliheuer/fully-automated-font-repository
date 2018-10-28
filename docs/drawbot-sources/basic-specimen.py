# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os


# STATIC VARIABLE
# WIDTH, HEIGHT, MARGIN, FRAMES
W,H,M,F = 1000,1000,100,30
VAR_WGHT = 300
LINE_H = H/10
START_POS = 800-4


# SET FONT
font("fonts/Foo-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID DRAWING FUNCTION
def grid(inc):
    stroke(0.4)
    stpX, stpY = 0, 0
    incX, incY = inc, inc
    for x in range(int(((W-(M*2))/inc)+1)):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(int(((H-(M*2))/inc)+1)):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

# DRAW NEW PAGE
newPage(W, H)
fill(0)
rect(0, 0, W, H)
grid(50)
fill(1)

# HEADLINE
tracking(0)
stroke(None)
fontSize(120)
fontVariations(wght=900)
text("Fully",      (M+10, (START_POS)-(0*LINE_H)))
text("Automated",  (M+10+4, (START_POS)-(1*LINE_H)))
text("Font",       (M+10, (START_POS)-(2*LINE_H)))
text("Repository", (M+10, (START_POS)-(3*LINE_H)))

# Draw large type
fontSize(50)
for i in range(6):
    VAR_WGHT += 100
    fontVariations(wght=VAR_WGHT)
    print("VAR_WGHT=", VAR_WGHT) 
    text("200. Foo-VF.ttf", (M+10+4, (START_POS-400+2)-(i*LINE_H/2)))

# Dot
oval(M+750, M, 50, 50)

# Draw small type
fontVariations(wght=400)
fill(1)
fontSize(50)
tracking(-4)
text("A B C D E F G H I J ", (M+400, (START_POS)-( 8*LINE_H/2)))
text("K L M N Q R S T U ", (M+400, (START_POS)-( 9*LINE_H/2)))
text("U W X Y Z ",  (M+400, (START_POS)-(10*LINE_H/2)))
text("a b c d e f g h i j k l",   (M+400, (START_POS)-(11*LINE_H/2)))
text("m n o p q r s t u v",   (M+400, (START_POS)-(12*LINE_H/2)))
text("w x y z",   (M+400, (START_POS)-(13*LINE_H/2)))

# Save GIF
os.chdir("docs")
os.chdir("specimens")
saveImage("basic-specimen.gif")
saveImage("basic-specimen.pdf")
os.chdir("..")
os.chdir("..")
