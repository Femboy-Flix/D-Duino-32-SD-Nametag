# ssd1306.py
# Treiber für SSD1306 OLED-Display
# Quelle: https://github.com/stlehmann/micropython-ssd1306

import framebuf


class SSD1306:
    def __init__(self, width, height, i2c, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.buffer = bytearray(self.width * self.height // 8)
        self.framebuf = framebuf.FrameBuffer(
            self.buffer, self.width, self.height, framebuf.MONO_VLSB
        )
        self.init_display()

    def init_display(self):
        for cmd in (
            0xAE,  # Display off
            0xD5, 0x80,  # Set display clock divide ratio/oscillator frequency
            0xA8, self.height - 1,  # Set multiplex ratio
            0xD3, 0x00,  # Set display offset
            0x40,  # Set start line address
            0x8D, 0x14,  # Enable charge pump
            0x20, 0x00,  # Set memory addressing mode
            0xA1,  # Set segment re-map
            0xC8,  # Set COM output scan direction
            0xDA, 0x12,  # Set COM pins hardware configuration
            0x81, 0xCF,  # Set contrast control
            0xD9, 0xF1,  # Set pre-charge period
            0xDB, 0x40,  # Set VCOMH deselect level
            0xA4,  # Entire display ON (resume to RAM content)
            0xA6,  # Set normal display
            0xAF,  # Display ON
        ):
            self.write_cmd(cmd)

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x80, cmd]))

    def write_data(self, data):
        self.i2c.writeto(self.addr, bytearray([0x40]) + data)

    def show(self):
        for page in range(0, self.height // 8):
            self.write_cmd(0xB0 + page)  # Set page address
            self.write_cmd(0x00)  # Set lower column start address
            self.write_cmd(0x10)  # Set higher column start address
            start = self.width * page
            end = start + self.width
            self.write_data(self.buffer[start:end])

    def fill(self, color):
        for i in range(len(self.buffer)):
            self.buffer[i] = 0xFF if color else 0x00

    def pixel(self, x, y, color):
        self.framebuf.pixel(x, y, color)

    def text(self, string, x, y):
        self.framebuf.text(string, x, y)

    def line(self, x1, y1, x2, y2, color):
        self.framebuf.line(x1, y1, x2, y2, color)
