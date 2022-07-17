from mplfinance.original_flavor import candlestick2_ochl, volume_overlay
import matplotlib.pyplot as plt
from exist_check import *
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import numpy as np 
from PIL import Image

plt.style.use('dark_background')

c = pd.DataFrame({"Date": [1, 3, 5, 7, 9], "Open" : [80, 95, 40, 25, 180], "Close": [40, 25, 80, 95, 180], "High" : [100, 100, 100, 100, 180], "Low" : [20, 20, 20, 20, 180]})
my_dpi = 96
fig, ax1 = plt.subplots(figsize=(1800 / my_dpi,
                            1800 / my_dpi), dpi=my_dpi)

# candlestick2_ochl(ax1, c.Open, c.Close, c.High, c.Low, width=0.5, colorup='#77d879', colordown='#db3f3f')

OFFSET = 0.5 / 2.0
lines = []
patches = []

for idx, q in c.iterrows():
    t, open, close, high, low = q[:5]
    
    if close >= open:
        color = '#77d879'
        lower = open
        height = close - open
    else:
        color = '#db3f3f'
        lower = close
        height = open - close

    vline = Line2D(
        xdata=(t, t), ydata=(low, high),
        color=color,
        linewidth=5,
        antialiased=True,
    )

    rect = Rectangle(
        xy=(t - OFFSET, lower),
        width=0.5,
        height=height,
        facecolor=color,
        edgecolor=color,
    )
    rect.set_alpha(1.0)

    lines.append(vline)
    patches.append(rect)
    ax1.add_line(vline)
    ax1.add_patch(rect)
ax1.autoscale_view()


ax1.grid(False)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.xaxis.set_visible(False)
ax1.yaxis.set_visible(False)
ax1.axis('off')

fig.canvas.draw()
np_array = np.array(fig.canvas.renderer._renderer)
# print(np_array)
pil_image=Image.fromarray(np_array)
rgb_image = pil_image.convert('RGB')

rgb_image.save("test1.png")

test = Image.open("test.png")
test_np = np.array(test)
print(test_np)
fig.savefig("test.png", pad_inches=0, transparent=False)
plt.close(fig)

