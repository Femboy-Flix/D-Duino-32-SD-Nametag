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
####################################################






    
    
    
    
    
    




####################################################  smylie zeichnen 
def draw_smiley(oled):
    oled.text("Felix", 1, 1)
    # Mittelpunkt und Radius des Kreises
    center_x = 64
    center_y = 32
    radius = 30

    # Kreis zeichnen (Rand des Gesichts)
    for angle in range(0, 360):
        x = int(center_x + radius * math.cos(math.radians(angle)))
        y = int(center_y + radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)

    # Augen (zwei kleine Kreise)
    eye_radius = 3
    left_eye_x, left_eye_y = 54, 24  # Position des linken Auges
    right_eye_x, right_eye_y = 74, 24  # Position des rechten Auges

    for angle in range(0, 360):
        # Linkes Auge
        x = int(left_eye_x + eye_radius * math.cos(math.radians(angle)))
        y = int(left_eye_y + eye_radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)

        # Rechtes Auge
        x = int(right_eye_x + eye_radius * math.cos(math.radians(angle)))
        y = int(right_eye_y + eye_radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)

    # Mund (umgedrehter Bogen)
    mouth_radius = 20
    mouth_start_angle = 20   # Beginn des Bogens
    mouth_end_angle = 160    # Ende des Bogens

    for angle in range(mouth_start_angle, mouth_end_angle):
        x = int(center_x + mouth_radius * math.cos(math.radians(angle)))
        y = int(center_y + mouth_radius * math.sin(math.radians(angle)))
        oled.pixel(x, y, 1)
#####################################################################UWU code 
def UWU():
            oled.fill(0)
            oled.text("FemboyFlix-Felix", 1, 1)
            oled.line(1, 10, 128, 10, 1)  # Horizontale Linie
    # "U" zeichnen
            oled.line(10, 20, 10, 60, 1)  # Linker Strich
            oled.line(10, 60, 30, 60, 1)  # Unterer Strich
            oled.line(30, 60, 30, 20, 1)  # Rechter Strich

    # "w" zeichnen
            oled.line(40, 20, 45, 60, 1)  # Linker Strich
            oled.line(45, 60, 50, 40, 1)  # Mittlerer linker Strich
            oled.line(50, 40, 55, 60, 1)  # Mittlerer rechter Strich
            oled.line(55, 60, 60, 20, 1)  # Rechter Strich

    # Zweites "U" zeichnen
            oled.line(70, 20, 70, 60, 1)  # Linker Strich
            oled.line(70, 60, 90, 60, 1)  # Unterer Strich
            oled.line(90, 60, 90, 20, 1)  # Rechter Strich
######################################################################FELIX code 
def FELIX():
    # "F" zeichnen
    oled.line(3, 10, 3, 60, 1)     # Linker Strich
    oled.line(3, 10, 30, 10, 1)    # Oberer horizontaler Strich
    oled.line(3, 35, 25, 35, 1)    # Mittlerer horizontaler Strich

    # "e" zeichnen
    oled.line(35, 35, 60, 35, 1)   # Mittlerer horizontaler Strich
    oled.line(35, 10, 60, 10, 1)   # Oberer horizontaler Strich
    oled.line(35, 60, 60, 60, 1)   # Unterer horizontaler Strich
    oled.line(35, 10, 35, 60, 1)   # Linker vertikaler Strich

    # "l" zeichnen
    oled.line(65, 10, 65, 60, 1)   # Vertikaler Strich
    oled.line(65, 60, 85, 60, 1)   # Unterer horizontaler Strich, der das "L" vervollständigt

    # "i" zeichnen
    oled.line(90, 20, 90, 60, 1)   # Vertikaler Strich
    oled.line(90, 10, 90, 16, 1)   # Punkt über dem "i"

    # "x" zeichnen
    oled.line(100, 10, 130, 60, 1)  # Diagonale von oben links nach unten rechts
    oled.line(130, 10, 100, 60, 1)  # Diagonale von oben rechts nach unten links
####################################################################### Webseite 
def WEB():
    oled.text("FemboyFlix-Felix", 1, 1)
    oled.line(1, 10, 128, 10, 1)  # Horizontale Linie
    oled.text("WEBSEITE:", 1, 12)
    oled.text("femboyflix.cc", 1, 22)
    oled.line(1, 32, 128, 32, 1)  # Horizontale Linie
######################################################################
def TXT():
    oled.text("FemboyFlix-Felix", 1, 1)
    oled.text("Hi 17 jo Hobbys:", 1, 12)
    oled.text("Foto,Video,codes", 1, 22)
    oled.text("crossdress,sleep", 1, 32)
    oled.text("sexuality : GAY", 1, 42)
    oled.text("just a Femboy", 1, 52)
###################################################################




















###################################prüft und setst den modus (bildschirm)
    
    
    
while True:
    chmode = mode 
    skle = skle + 1
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
        
        
        
        
        
        
        
    if not button_5.value():
        print("button5")
        time.sleep(0.3)  # Entprellzeit
        
        if ledmode == 0 :
            np[0] = (50, 0, 25)  # (Rot, Grün, Blau) g
            np.write()
            ledmode = 1
            
            
        elif ledmode == 1 :
            np[0] = (0, 0, 0)  # (Rot, Grün, Blau)
            np.write()
            ledmode = 0



####################################

    if not button_select.value():
        print("Seleckt")
        mode = random.randint(0, 4)
      
        
        if swmode == 0 :
            oled.fill(0)
            swmode =1
            oled.text("Mode Randeom", 1, 1)
            oled.show()
            time.sleep(2)
            
        elif swmode == 1 :
            oled.fill(0)
            swmode = 0
            oled.text("Mode Static", 1, 1)
            oled.show()
            time.sleep(2)
######################################
     
     
     
     
     
     
     
#####################################random modi      
    if swmode == 1 and skle > 10 :
        skle = 0
        mode = random.randint(0, 4)
        
    
################modi 
    if mode > 4:
        mode = 4
    if mode < 0:
        mode = 0
##################################



















################################################################ verschiedenen anzeigen 
#nur mei modusänderung 
    if mode != chmode:
        oled.fill(0) # Bildschirm leeren
        
        if mode == 0:
            UWU()
            
           
        elif mode == 1:
             WEB()
            
        elif mode == 2:
             FELIX()
           
        
        elif mode == 3:
            draw_smiley(oled)
           
            
        elif mode == 4:
            TXT()
            
        oled.show()
        np.write()