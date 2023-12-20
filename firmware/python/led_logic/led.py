""" Create a class for the LED """

import time
import neopixel
import board


class LED:
    """Create a class for the LED"""

    def __init__(self):
        """Initialize the LED"""
        self.pixels = neopixel.NeoPixel(board.D18, 1, brightness=100, auto_write=False)
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def set_color(self, red, green, blue):
        """Set the color of the LED"""
        self.pixels.fill((red, green, blue))
        self.pixels.show()

    def fade(self, red, green, blue, duration):
        """Fade the LED to the specified color over the specified duration"""
        current_color = self.pixels[0]
        current_red = current_color[0]
        current_green = current_color[1]
        current_blue = current_color[2]
        red_step = (red - current_red) / duration
        green_step = (green - current_green) / duration
        blue_step = (blue - current_blue) / duration
        for i in range(duration):
            self.pixels.fill(
                (
                    int(current_red + (red_step * i)),
                    int(current_green + (green_step * i)),
                    int(current_blue + (blue_step * i)),
                )
            )
            self.pixels.show()
            time.sleep(1)
        self.pixels.fill((red, green, blue))
        self.pixels.show()

    def rainbow_cycle(self, wait):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(255):
            for i in range(len(self.pixels)):
                idx = int((i * 256 / len(self.pixels)) + j)
                self.pixels[i] = self.wheel(idx & 255)
            self.pixels.show()
            time.sleep(wait)


if __name__ == "__main__":
    strip = LED
    strip.set_color(255, 0, 0)
