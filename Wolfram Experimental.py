import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr, wl
session = WolframLanguageSession()
command = 'Export["plot.png", Plot[Sin[x], {x, 0, 2 Pi}]]'

session.evaluate(command)

img = mpimg.imread('plot.png')
plt.imshow(img)
plt.axis('off')
plt.show()