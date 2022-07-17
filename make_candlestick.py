from mplfinance.original_flavor import candlestick2_ochl, volume_overlay
import matplotlib.pyplot as plt
from exist_check import *
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
import pickle as pl
import numpy as np
from PIL import Image
from Model import *

# moving average column name
def makeIndex(ma):
    return 'ma_' + str(ma)

# color of moving average
def set_ma_style(ma):
    if ma == 'ma_5' :
        color = '#0061cb'
    elif ma == 'ma_20':
        color = '#efbb00'
    elif ma == 'ma_60':
        color = '#ff4aad'
    elif ma == 'ma_120':
        color ='#882dff'
    else :
        color = '#ffffff'
    
    return color

def make_candlestick(path, type, ticker, date, label, labeling, dp, fore, size, is_vol, MAs, df):
    count = 0
    plt.style.use('dark_background')
    
    x = df.index[df['Date'] == date].tolist()[0]
    c = df.iloc[x:x + int(dp), :]
    c.reset_index(inplace=True)

    if len(c) == int(dp):
        my_dpi = 96
        fig, ax1 = plt.subplots(figsize=(size[0] / my_dpi,
                                    size[1] / my_dpi), dpi=my_dpi)
        
        candlestick2_ochl(ax1, c.Open, c.Close, c.High, c.Low, width=1,  colorup='#77d879', colordown='#db3f3f')
        if MAs != [-1]:
            MAstr = list(map(makeIndex, MAs))
            for ma in MAstr :
                ax1.plot(c[ma], linewidth=0.8, color=set_ma_style(ma))
        ax1.grid(False)
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax1.xaxis.set_visible(False)
        ax1.yaxis.set_visible(False)
        ax1.axis('off')

        # create the second axis for the volume bar-plot
        # Add a seconds axis for the volume overlay
        if is_vol:
            #is_vol = '_vol'
            ax2 = ax1.twinx()
            # Plot the volume overlay
            bc = volume_overlay(ax2, c['Open'], c['Close'], c['Volume'],
                                colorup='#77d879', colordown='#db3f3f', alpha=0.5, width=1)
            ax2.add_collection(bc)
            ax2.grid(False)
            ax2.set_xticklabels([])
            ax2.set_yticklabels([])
            ax2.xaxis.set_visible(False)
            ax2.yaxis.set_visible(False)
            ax2.axis('off')
        
        # plt.tight_layout()
        # fig.savefig(path, pad_inches=0, bbox_inches='tight', transparent=False)
        name = path.label_dic[type][label] + path.image_name(ticker, date, is_vol, MAs, dp, fore, labeling, label)
        
        fig.canvas.draw()
        np_array = np.array(fig.canvas.renderer._renderer)
        pil_image=Image.fromarray(np_array)
        rgb_image = pil_image.convert('RGB')
        rgb_image.save(name)
        
        # fig.savefig(name, pad_inches=0, transparent=False)
        count += 1
        plt.close(fig)
    # normal length - end
    
'''
def candlestick2_ochl(ax, o, c, h, l, width, linewidth, colorup, colordown) :
    OFFSET = 0.5 / 2.0
    lines = []
    patches = []
    
    for i in range(len(o)):
        open = o[i]
        close = c[i]
        high = h[i]
        low = l[i]
        
        if close >= open:
            color = colorup
            lower = open
            height = close - open
        else:
            color = colordown
            lower = close
            height = open - close

        vline = Line2D(
            xdata=(i, i), ydata=(low, high),
            color=color,
            linewidth=linewidth,
            antialiased=True,
        )

        rect = Rectangle(
            xy=(i - OFFSET, lower),
            width=width,
            height=height,
            facecolor=color,
            edgecolor=color,
        )
        rect.set_alpha(1.0)

        lines.append(vline)
        patches.append(rect)
        ax.add_line(vline)
        ax.add_patch(rect)
    ax.autoscale_view()
 '''