import subprocess
import sys
import time

sys.path.append("../..") # set system path to top
from devices import dfrobot_epaper
from display_extension.freetype_helper import Freetype_Helper
fontFilePath = "../../display_extension/wqydkzh.ttf" # fonts file

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
epaper.begin()
epaper.clearScreen();
# config extension fonts
ft = Freetype_Helper(fontFilePath)
ft.setDisLowerLimite(75) # set display lower limit, adjust this to effect fonts color depth
epaper.setExFonts(ft) # init with fonts file
epaper.setTextFormat(1, epaper.WHITE, epaper.BLACK, 1, 1)

ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

try:
    output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
    out = output.decode("utf-8")
    print(out)
    # epaper
    epaper.setExFontsFmt(20, 20) # set extension fonts width and height
    epaper.setTextCursor(0, 0)
    epaper.printStr(out)
    epaper.setTextFormat(1, epaper.BLACK, epaper.WHITE, 1, 1)
    epaper.setExFontsFmt(18, 18) # set extension fonts width and height
    epaper.setTextCursor(0, 50)
    quote = "'One original thought is worth a thousand mindless quotings.' ― Diogenes"
    epaper.printStr(quote)
    epaper.begin()
    epaper.flush(epaper.PART)
    time.sleep(1)
except subprocess.CalledProcessError:
    # grep did not match any lines
    print("No wireless networks connected")
     # epaper
    epaper.setExFontsFmt(20, 20) # set extension fonts width and height
    epaper.setTextCursor(0, 0)
    epaper.printStr("No wireless networks  ")
    epaper.setTextFormat(1, epaper.BLACK, epaper.WHITE, 1, 1)
    epaper.setExFontsFmt(19, 19) # set extension fonts width and height
    epaper.setTextCursor(0, 30)
    quote = "'It is possible to fail in many ways...while to succeed is possible only in one way.' - Aristotle"
    epaper.printStr(quote)
    epaper.begin()
    epaper.flush(epaper.PART)
    time.sleep(1)
