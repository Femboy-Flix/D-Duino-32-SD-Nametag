

# README

## Project: Multi-Display Modes on an OLED with the DSTIKE D-Duino-32

This project demonstrates how to display various modes on an OLED screen using the DSTIKE D-Duino-32, an ESP32-based board. The project includes interactive features like buttons for mode selection and a NeoPixel LED for additional effects.

### Features
- **OLED Display Modes**: Displays text, graphics, and animations like a smiley or custom text.
- **Interactive Buttons**: Navigate through different modes using buttons.
- **NeoPixel LED Control**: Toggle the NeoPixel LED on/off with a button press.
- **Random Mode**: Automatically switch to a random mode.

---

### Requirements
1. **Hardware**:
   - DSTIKE D-Duino-32 (or equivalent ESP32 board with OLED).
   - Buttons connected to pins 25, 32, 33, and 5.
   - NeoPixel LED connected to pin 18.
   - I2C OLED display (connected to SDA: Pin 26, SCL: Pin 27).

2. **Software**:
   - [Thonny IDE](https://thonny.org/) (Python programming environment).
   - The following libraries installed on the ESP32:
     - `ssd1306`: For controlling the OLED display.
     - `neopixel`: For controlling the NeoPixel LED.

---

### Setup Instructions

#### 1. Install Thonny IDE
- Download and install the Thonny IDE from [thonny.org](https://thonny.org/).
- Select the "MicroPython (ESP32)" interpreter in Thonny.

#### 2. Flash MicroPython on the ESP32
- Follow [this guide](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html) to flash MicroPython onto your ESP32 board.

#### 3. Install Required Libraries
- Copy the `ssd1306.py` library file to your ESP32 board.
  - You can download it from [this GitHub repository](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py).
- Use the `neopixel` library, which is built into MicroPython for ESP32.

#### 4. Upload the Code
1. Open `boot.py` in Thonny.
2. Connect your DSTIKE D-Duino-32 to your computer via USB.
3. Click **Run** > **Upload current script as main script** to save the file on the ESP32.

---

### Wiring Diagram
| Component         | Pin       |
|-------------------|-----------|
| OLED SDA          | GPIO 26   |
| OLED SCL          | GPIO 27   |
| Button Up         | GPIO 32   |
| Button Down       | GPIO 25   |
| Button Select     | GPIO 33   |
| Button 5 (LED)    | GPIO 5    |
| NeoPixel LED      | GPIO 18   |

---

### Usage
1. Power on your D-Duino-32. 
2. Use the buttons to navigate through the modes:
   - **Button Up**: Move to the next mode.
   - **Button Down**: Move to the previous mode.
   - **Button Select**: Switch between random mode and static mode.
   - **Button 5**: Toggle the NeoPixel LED on/off.
3. The OLED display will show different visuals depending on the selected mode:
   - **Mode 0**: Displays "UWU" text and graphics.
   - **Mode 1**: Displays the website information ("femboyflix.cc").
   - **Mode 2**: Draws the text "FELIX" in a custom font.
   - **Mode 3**: Draws a smiley face.
   - **Mode 4**: Displays personal text information.

---

### Troubleshooting
- **No Display**: Check the I2C connections (SDA and SCL).
- **NeoPixel Not Lighting**: Ensure the LED is connected to GPIO 18 and the power supply is sufficient.
- **Button Issues**: Confirm correct wiring and pull-up resistor configuration.

---

### License
This project is open-source and can be modified or shared as needed. Attribution is appreciated.

--- 
