# -*- coding:utf-8 -*-
'''
file demo_print.py

connect epaper to your raspberryPi
print with fonts file, Different files will have different display effects

Copyright   [DFRobot](http://www.dfrobot.com), 2016
Copyright   GNU Lesser General Public License

version  V1.0
date  2018-10-27
'''

import sys
import time
sys.path.append("../..") # set system path to top

from devices import dfrobot_epaper
import time
import threading


# peripheral params
RASPBERRY_SPI_BUS = 0
RASPBERRY_SPI_DEV = 0
RASPBERRY_PIN_CS = 27
RASPBERRY_PIN_CD = 17
RASPBERRY_PIN_BUSY = 4

# get gpio interface
GPIO = dfrobot_epaper.GPIO
EPAPER_KEY_A = 21
EPAPER_KEY_B = 20

epaper = dfrobot_epaper.DFRobot_Epaper_SPI(RASPBERRY_SPI_BUS, RASPBERRY_SPI_DEV, RASPBERRY_PIN_CS, RASPBERRY_PIN_CD, RASPBERRY_PIN_BUSY) # create epaper object


from display_extension.freetype_helper import Freetype_Helper
import requests
fontFilePath = "../../display_extension/wqydkzh.ttf" # fonts file


url='https://www.reddit.com/r/quotes/hot/.json'
params = dict(t='hour', limit='1')
resp = requests.get(url=url, params=params, headers={'User-agent':'EDP-EXAMPLE 0.1'})
json = resp.json()
#print(json)
data = json['data']['children'][0]['data']['title']

# Use built in module "textwrap" to format the string into a paragraph
import textwrap
wrapper = textwrap.TextWrapper(width=22)
quote = wrapper.wrap(text=data)
quote = '\n'.join(quote)
print(len(quote))

epaper.begin()
epaper.clearScreen();
# config extension fonts
ft = Freetype_Helper(fontFilePath)
ft.setDisLowerLimite(75) # set display lower limit, adjust this to effect fonts color depth
epaper.setExFonts(ft) # init with fonts file
epaper.setTextFormat(1, epaper.BLACK, epaper.WHITE, 1, 1)

if (len(quote) > 200):
    epaper.setExFontsFmt(13, 13) # set extension fonts width and height
    wrapper = textwrap.TextWrapper(width=35)
    quote = wrapper.wrap(text=data)
    quote = '\n'.join(quote)    
if (len(quote) > 160 and len(quote) <= 200):
    epaper.setExFontsFmt(18, 14) # set extension fonts width and height
    wrapper = textwrap.TextWrapper(width=25)
    quote = wrapper.wrap(text=data)
    quote = '\n'.join(quote)
if (len(quote) > 120 and len(quote) <= 160):
    epaper.setExFontsFmt(18, 16) # set extension fonts width and height
    wrapper = textwrap.TextWrapper(width=25)
    quote = wrapper.wrap(text=data)
    quote = '\n'.join(quote)
    print('here')
if (len(quote) <= 120):
    epaper.setExFontsFmt(20, 20) # set extension fonts width and height

# print test
epaper.setTextCursor(0, 0)
epaper.printStr(quote)
epaper.begin()
epaper.flush(epaper.PART)
time.sleep(1)
