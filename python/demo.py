from builder import *
import os

x = Site("x")
x.directoryDraw()
x.noConfigDraw()
os.chdir("x")
x.siteDraw()
