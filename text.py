from cProfile import label
import tkinter as tk
from PIL import ImageTk
from urllib.request import urlopen

root = tk.Tk()

imageUrl = "https://www.pythontutorial.net/wp-content/uploads/2021/01/Tkinter-grid-Sticky-EW.png"
u = urlopen(imageUrl)
raw_data = u.read()
u.close()

photo = ImageTk.PhotoImage(data=raw_data)
label = tk.Label(image=photo)
label.image = photo
label.pack()

root.mainloop()

# ''' turtle_Tk_Canvas_Image_url.py
# display a GIF image obtained from an internet web page
# on a Tkinter canvas, then use the canvas for some turtle drawing
# modified Vegaseat code
# '''

# import io
# import base64
# import turtle
# try:
#     # Python2
#     import Tkinter as tk
#     from urllib2 import urlopen
# except ImportError:
#     # Python3
#     import tkinter as tk
#     from urllib.request import urlopen


# root = tk.Tk()
# root.title("turtle graphics a website image")

# # this GIF picture previously downloaded to tinypic.com
# image_url = "http://i46.tinypic.com/r9oh0j.gif"

# image_byt = urlopen(image_url).read()
# image_b64 = base64.encodestring(image_byt)
# photo = tk.PhotoImage(data=image_b64)

# # create a white canvas large enough to fit the image+
# w = 540
# h = 340
# cv = tk.Canvas(bg='white', width=w, height=h)
# cv.pack()

# # this makes the canvas a turtle canvas
# # point(0, 0) is in the center now
# tu = turtle.RawTurtle(cv)

# # put the image on the turtle canvas with
# # create_image(xpos, ypos, image, anchor)
# xpos = int(w/2 * 0.9)
# ypos = int(h/2 * 0.9)
# print(xpos, ypos)
# cv.create_image(-xpos, -ypos, image=photo, anchor='nw')

# # now do some turtle graphics
# tu.pensize(2)
# for radius in range(50, 200, 40):
#     # pen up
#     tu.up()
#     # move pen to point x, y
#     # keeps the center of the circle at canvas center
#     tu.goto(0, -radius)
#     # pen down
#     tu.down()
#     tu.circle(radius)

# root.mainloop()
