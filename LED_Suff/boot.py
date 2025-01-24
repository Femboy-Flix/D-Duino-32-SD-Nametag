############################################### import und dafinition 
from machine import Pin, I2C
import framebuf
from ssd1306 import SSD1306
import time
import math
import random
from machine import Pin
import neopixel
import machine

# Display-Größe
WIDTH = 130
HEIGHT = 64

# I2C einrichten (SDA=26, SCL=27, wie im GitHub-Repository beschrieben)
i2c = I2C(0, scl=Pin(27), sda=Pin(26))

# initialisieren
oled = SSD1306(WIDTH, HEIGHT, i2c)
button_up = Pin(32, Pin.IN, Pin.PULL_UP)
button_down = Pin(25, Pin.IN, Pin.PULL_UP)
button_select = Pin(33, Pin.IN, Pin.PULL_UP)
np = neopixel.NeoPixel(machine.Pin(18), 1)
button_5= Pin(5, Pin.IN, Pin.PULL_UP)

# Bild auf das Display zeichnen
def show_image():
    oled.fill(1)  # Bildschirm leeren
    oled.write_data(image_data)  # Bilddaten auf das Display senden
    oled.show()  # Aktualisiere die Anzeige


mode = 0  # Start Bildschirm
chmode = -1  # Initialisierter Vergleichsmodus, um Änderungen zu erkennen
swmode = 0
skle = 0 #durchlaüfe des programmes

ledmode = 0

sett = 0
opt = 0
lock = 0
modeset = 0

    
while True:
    chmode = mode 
    time.sleep(0.4)
    
    print("round")
    print(mode)

    # Prüfe die Buttons
    if not button_up.value():
        print("up")
        time.sleep(0.3)  # Entprellzeit
        mode += 1

    if not button_down.value():
        print("down")
        time.sleep(0.3)  # Entprellzeit
        mode -= 1
        

    if mode > 3:
        mode = 3
    if mode < 0:
        mode = 0

    if mode != chmode:
        oled.fill(0) # Bildschirm leeren
        
        if mode == 0:
            oled.text("Rot", 1, 1)
            np[0] = (255, 0, 0)
        elif mode == 1:
            oled.text("Grün", 1, 1)
            np[0] = (0, 255, 0)
        elif mode == 2:
            oled.text("Blau", 1, 1)
            np[0] = (0, 0, 255)
        elif mode == 3:
            oled.text("Pink", 1, 1)
            np[0] = (255, 0, 125)
        oled.show()
        np.write()